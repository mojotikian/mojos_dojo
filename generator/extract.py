# Build pools.json: every manifest variant of each owned random-roll weapon, with columns, part stats and base stats.
# Input: owned.txt (comma-separated item hashes from DIM), ../items.json, ../plugsets.json, ../statdefs.json
import json, collections
I = json.load(open('../items.json')); P = json.load(open('../plugsets.json')); S = json.load(open('../statdefs.json'))
sn = lambda h: S.get(str(h), {}).get('displayProperties', {}).get('name', '')
d = lambda h: I.get(str(h), {})
def clean(n):
    for s in [' (Adept)', ' (Timelost)', ' (Harrowed)', ' (Baroque)']: n = n.replace(s, '')
    return n
owned = open('owned.txt').read().strip().split(',')
PERKCATS = {'frames','barrels','magazines','tubes','magazines_gl','batteries','blades','guards','bowstrings','arrows',
            'hafts','scopes','stocks','grips','rails','bolts','v950.new.sword0.blades','v950.new.sword0.guards'}
def pool(v, s):
    # random-roll socket, or (fixed-roll weapon) a perk socket with selectable options (Komodo-4FR case, v2.2)
    if s.get('randomizedPlugSetHash'): return s['randomizedPlugSetHash']
    if fixed(v) and s.get('reusablePlugSetHash') and d(s.get('singleInitialItemHash')).get('plug', {}).get('plugCategoryIdentifier') in PERKCATS:
        return s['reusablePlugSetHash']
    return None
def fixed(v):
    se = v.get('sockets', {}).get('socketEntries', [])
    if any(s.get('randomizedPlugSetHash') for s in se): return False
    fr = [s for s in se if d(s.get('singleInitialItemHash')).get('plug', {}).get('plugCategoryIdentifier') == 'frames' and s.get('reusablePlugSetHash')]
    return len(fr) >= 2 and all(len(P.get(str(s['reusablePlugSetHash']), {}).get('reusablePlugItems', [])) > 1 for s in fr)
rand = lambda v: any(s.get('randomizedPlugSetHash') for s in v.get('sockets', {}).get('socketEntries', [])) or fixed(v)
names = {clean(d(h)['displayProperties']['name']) for h in owned if rand(d(h))}
out = {}
for h, v in I.items():
    if v.get('itemType') != 3 or not rand(v): continue
    n = clean(v.get('displayProperties', {}).get('name', ''))
    if n not in names: continue
    cols = []
    for s in v['sockets']['socketEntries']:
        r = pool(v, s)
        if not r: continue
        pl, seen = [], set()
        for x in P.get(str(r), {}).get('reusablePlugItems', []):
            if not x.get('currentlyCanRoll', True) or x['plugItemHash'] in seen: continue
            pd = d(x['plugItemHash'])
            if pd.get('itemTypeDisplayName', '').startswith('Enhanced'): continue  # base hashes only
            seen.add(x['plugItemHash'])
            st = {sn(i['statTypeHash']): i['value'] for i in pd.get('investmentStats', []) if i.get('value') and sn(i['statTypeHash'])}
            pl.append({'h': x['plugItemHash'], 'n': pd.get('displayProperties', {}).get('name'), 'c': pd.get('plug', {}).get('plugCategoryIdentifier', ''), 'st': st})
        if pl: cols.append(pl)
    stats = {sn(k): val['value'] for k, val in v.get('stats', {}).get('stats', {}).items() if sn(k)}
    intr = [d(s.get('singleInitialItemHash')).get('displayProperties', {}).get('name') for s in v['sockets']['socketEntries']
            if d(s.get('singleInitialItemHash')).get('plug', {}).get('plugCategoryIdentifier') == 'intrinsics']
    out[h] = {'name': n, 'full': v['displayProperties']['name'], 'type': v.get('itemTypeDisplayName'),
              'tier': v['inventory'].get('tierTypeName'), 'dmg': v.get('defaultDamageType'),
              'frame': (intr or [None])[0], 'stats': stats, 'cols': cols, 'owned': h in owned}
json.dump(out, open('pools.json', 'w'))
print('weapons', len(names), 'variant hashes', len(out))
