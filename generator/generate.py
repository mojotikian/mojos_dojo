import json, re, itertools, collections, sys
sys.path.insert(0, '.')
from rules import *

I = json.load(open('../items.json'))
D = json.load(open('pools.json'))
VERSION = 'v2.2'
PRIORITY = ['PVE','PVP','ELEM','ABTY','UTLY','JKPT']  # Paul's tie order (2026-10-25); also note tag order
DMG = {1:'kinetic',2:'arc',3:'solar',4:'void',6:'stasis',7:'strand'}
PARTCATS = {'barrels','magazines','tubes','magazines_gl','batteries','blades','guards','bowstrings','arrows',
            'hafts','scopes','stocks','grips','rails','bolts','v950.new.sword0.blades','v950.new.sword0.guards'}

def additive(p):
    for k,v in p['st'].items():
        if k in NEG_GOOD:
            if v > 0: return False
        elif v < 0: return False
    return p['n'] not in BANNED_PARTS

def penalty(p):
    return sum((-v if k in NEG_GOOD else v) for k,v in p['st'].items())

def part_choices(w, col, jackpot=False):
    cat = col[0]['c']
    # Rule 4b swords
    if 'blades' in cat and not jackpot:
        f = [p for p in col if p['n']=='Tempered Edge']
        if f: return f
    if 'guards' in cat and not jackpot:
        f = [p for p in col if p['n']=='Enduring Guard'] or [p for p in col if p['n']=='Burst Guard']
        if f: return f
    add = [p for p in col if additive(p)]
    if not add:  # glaives/forced pools: least penalty
        return sorted([p for p in col if p['n'] not in BANNED_PARTS], key=penalty, reverse=True)[:3 if not jackpot else 99]
    if jackpot:
        return add
    stats = w['stats']
    present = [s for s in DEFSTATS if s in stats and stats[s] > 0]
    weak = sorted(present, key=lambda s: stats[s])[:2]
    def sc(p):
        s = sum(2*p['st'].get(k,0) for k in weak)
        tot = sum((-v if k in NEG_GOOD else v) for k,v in p['st'].items())
        return s + 0.2*tot
    return sorted(add, key=sc, reverse=True)[:3]

def weak_stats(w):
    stats = w['stats']; present = [s for s in DEFSTATS if s in stats and stats[s] > 0]
    return sorted(present, key=lambda s: stats[s])[:2]

def pairs(c3, c4):
    out = []
    for a in c3:
        for b in c4:
            if a['n'] == b['n']: continue
            if a['n'] in INTRINSIC_FRAMES or b['n'] in INTRINSIC_FRAMES: continue
            out.append((a, b))
    return out

def elem_ok(t, wel):
    e = ELEM.get(t)
    return e is not None and (e == 'any' or e == wel or wel == 'kinetic')

def choose(w):
    fc = [c for c in w['cols'] if c[0]['c'] == 'frames']
    if len(fc) < 2: return {}
    c3, c4 = fc[-2], fc[-1]
    P = pairs(c3, c4)
    if not P: return {}
    wt = w['type']; wel = DMG.get(w['dmg'], 'kinetic')
    g = lambda t,i: T.get(t,(0,3,0))[i]
    res = {}
    # PVE
    best = max(P, key=lambda p: g(p[0]['n'],1)+g(p[1]['n'],1)+PVE_PAIRS.get(frozenset([p[0]['n'],p[1]['n']]),0))
    res['PVE'] = [best]
    # PVP: both perks must work before the kill
    pv = [(pvp_val(a['n'],wt)+pvp_val(b['n'],wt),a,b) for a,b in P if min(pvp_val(a['n'],wt),pvp_val(b['n'],wt)) >= 3]
    if pv:
        s,a,b = max(pv, key=lambda x:x[0])
        if s >= 9: res['PVP'] = [(a,b)]
    # UTLY
    ut = [(g(a['n'],2)+g(b['n'],2),a,b) for a,b in P if min(g(a['n'],2),g(b['n'],2)) >= 4]
    if ut:
        s,a,b = max(ut, key=lambda x:x[0]); res['UTLY'] = [(a,b)]
    # ELEM: 2a chains first, then 2b cross-column elemental pairings, cap 4
    el = []
    for a,b in P:
        fs = frozenset([a['n'],b['n']])
        if fs in CHAINSET: el.append((100+g(a['n'],1)+g(b['n'],1),a,b))
        elif elem_ok(a['n'],wel) and elem_ok(b['n'],wel): el.append((g(a['n'],1)+g(b['n'],1),a,b))
    if el: res['ELEM'] = [(a,b) for s,a,b in sorted(el, key=lambda x:-x[0])[:4]]
    # ABTY: same family or gen->payoff, cap 2
    ab = []
    for a,b in P:
        fs = frozenset([a['n'],b['n']]); fa, fb = FAMILY.get(a['n']), FAMILY.get(b['n'])
        if fs in ABTY_PAIRS or (fa and fa == fb and fa != 'gen'):
            ab.append((g(a['n'],1)+g(b['n'],1),a,b))
    if ab: res['ABTY'] = [(a,b) for s,a,b in sorted(ab, key=lambda x:-x[0])[:2]]
    return res

def lines_for(h, w, tag, pair, jackpot):
    pcols = [c for c in w['cols'] if c[0]['c'] in PARTCATS]
    choices = [part_choices(w, c, jackpot) for c in pcols]
    weak = weak_stats(w)
    a, b = pair
    note = (f"[{tag}] 5/5 {w['name']}: {a['n']} + {b['n']}" if tag != 'JKPT'
            else f"[JKPT] jackpot {w['name']}: {a['n']} + {b['n']}, any additive parts")
    if tag != 'JKPT' and weak: note += f"; parts aimed at {'/'.join(weak)}"
    note += f" (Mojo's Dojo {VERSION})"
    out = []
    for combo in (itertools.product(*choices) if choices else [()]):
        perks = [a['h'], b['h']] + [p['h'] for p in combo]
        out.append((h, tuple(perks), note))
    return out

jk, body = [], []
ledger = collections.OrderedDict()
skipped = collections.Counter()
for h, w in sorted(D.items(), key=lambda x: (x[1]['type'], x[1]['name'])):
    if w['tier'] != 'Legendary': skipped['exotic/other'] += 1; continue
    res = choose(w)
    if not res: skipped['no trait pairs'] += 1; continue
    led = ledger.setdefault(w['name'], {'type': w['type'], 'frame': w['frame'], 'element': DMG.get(w['dmg'], 'kinetic'),
                                        'weak': weak_stats(w), 'variants': [], 'picks': {}, 'targets': {}})
    led['variants'].append(int(h))
    pcols = [c for c in w['cols'] if c[0]['c'] in PARTCATS]
    for tag in PRIORITY[:-1]:
        for pair in res.get(tag, []):
            body += lines_for(h, w, tag, pair, False)
            jk += lines_for(h, w, 'JKPT', pair, True)
            led['picks'].setdefault(tag, set()).add(f"{pair[0]['n']} + {pair[1]['n']}")
            key = f"{pair[0]['n']} + {pair[1]['n']}"
            tl = led['targets'].setdefault(tag, {})
            if key not in tl:  # trait hashes accumulate across variants (Adept/reissue share names, hashes usually identical)
                tl[key] = {'traits': [[pair[0]['n']], [pair[1]['n']]], 'trait_hashes': [[], []],
                           'parts': [sorted({p['n'] for p in part_choices(w, c)}) for c in pcols]}
            for i in (0, 1):
                if pair[i]['h'] not in tl[key]['trait_hashes'][i]: tl[key]['trait_hashes'][i].append(pair[i]['h'])

# merge: one line per item+perkset, note lists every tag it satisfies
M = collections.OrderedDict()
for h, perks, note in jk + body:
    key = (h, frozenset(perks))
    tag = note.split(']')[0][1:]
    e = M.setdefault(key, {'perks': perks, 'tags': [], 'five': None, 'jk': None})
    if tag not in e['tags']: e['tags'].append(tag)
    if tag == 'JKPT': e['jk'] = e['jk'] or note
    else: e['five'] = e['five'] or note
ORDER = PRIORITY
final = []
for (h,_), e in M.items():
    tags = ''.join(f'[{t}]' for t in ORDER if t in e['tags'])
    base = e['five'] or e['jk']
    body_txt = base.split('] ',1)[1]
    if e['five'] is None: body_txt = body_txt  # jackpot-only combo
    final.append((h, e['perks'], tags + ' ' + body_txt))
# ---------- validation gates ----------
bad = enh = sub4 = 0
rx = re.compile(r'^dimwishlist:item=\d+&perks=\d+(,\d+)*#notes:.+$')
text = []; blocks = []; prev = None
for h, perks, note in final:
    if note != prev:
        if prev is not None: blocks.append('')
        blocks.append('//notes:' + note); prev = note
    blocks.append(f"dimwishlist:item={h}&perks={','.join(str(p) for p in perks)}")
    line = f"dimwishlist:item={h}&perks={','.join(str(p) for p in perks)}#notes:{note}"
    if not rx.match(line): bad += 1
    for p in perks:
        if I.get(str(p),{}).get('itemTypeDisplayName','').startswith('Enhanced'): enh += 1
    if len(perks) < 4: sub4 += 1
    text.append(line)
dupes = len(text) - len(set(text))
hdr = [f"title:Mojo's Dojo {VERSION}",
       "description:Paul's 5/5 godroll compendium. Tags in priority order: [PVE] [PVP] [ELEM] [ABTY] [UTLY] [JKPT]. Base hashes only.",
       f"// {VERSION}: {len(ledger)} owned random-roll legendaries, every Adept/reissue variant. Live: raw.githubusercontent.com/mojotikian/mojos_dojo/main/mojos_dojo.txt"]
jk_n = len(text)
out = hdr + ['// One line per roll; the note lists every category it satisfies, in priority order. [JKPT] = any additive parts.', ''] + blocks
open('mojos_dojo.txt','w').write('\n'.join(out) + '\n')
json.dump({'version': VERSION, 'priority': PRIORITY,
           'weapons': {k:{**v,'picks':{t:sorted(s) for t,s in v['picks'].items()}} for k,v in ledger.items()}},
          open('ledger.json','w'), indent=1)
tagc = collections.Counter(t for _,_,n in final for t in re.findall(r'\[(\w+)\]', n.split(' ')[0]))
wc = collections.Counter(t for v in ledger.values() for t in v['picks'])
print('weapons', len(ledger), 'lines', len(text), 'by tag', dict(tagc))
print('weapons with each tag', dict(wc))
print('GATES bad', bad, 'dupes', dupes, 'enhanced', enh, 'sub4', sub4, 'skipped', dict(skipped))
import os; print('size MB', round(os.path.getsize('mojos_dojo.txt')/1e6, 2))
