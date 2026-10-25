# Mojo's Dojo rule tables. Scores 0-10. Unlisted traits: pve 3, pvp 0, utl 0.
# T[name] = (pvp, pve, utl)   pvp counts ONLY if the perk works before the kill.
T = {
 # --- precision / neutral game (pre-kill) ---
 'Opening Shot':(8,3,0),'Rangefinder':(7,4,0),'Snapshot Sights':(8,3,0),'Quickdraw':(8,2,0),
 'Moving Target':(7,1,3),'Keep Away':(7,2,0),'Eye of the Storm':(5,3,0),'Threat Detector':(6,4,0),
 'Zen Moment':(5,3,0),'Tap the Trigger':(6,3,0),'Dynamic Sway Reduction':(6,3,0),'Target Lock':(7,7,0),
 'Perpetual Motion':(5,3,6),'Lone Wolf':(5,4,0),'Slideshot':(6,5,3),'Slideways':(6,3,4),'Air Assault':(5,2,4),
 'Steady Hands':(5,2,0),'Iron Gaze':(5,4,0),'Iron Grip':(5,2,0),'Iron Reach':(5,2,0),'Hip-Fire Grip':(5,2,0),
 'Firmly Planted':(4,2,0),'Under Pressure':(4,4,0),'High Ground':(4,2,0),'Fragile Focus':(4,3,0),
 'Box Breathing':(6,6,0),'Headseeker':(6,4,0),'Elemental Capacitor':(4,5,0),'Slickdraw':(6,2,0),
 'Sleight of Hand':(4,4,0),'Tunnel Vision':(3,3,0),'Turnabout':(4,3,0),'Pulse Monitor':(4,3,3),
 'Close to Melee':(4,4,0),'Pugilist':(4,4,0),'Trench Barrel':(5,7,0),'Dual Loader':(4,3,4),
 'Disruption Break':(3,5,0),'Under-Over':(3,6,2),'Danger Zone':(3,5,0),'Barrel Constrictor':(3,3,0),
 'Compulsive Reloader':(3,3,0),'Chill Clip':(4,7,0),'Precision Instrument':(4,7,0),'Celerity':(3,3,4),
 'Encore':(0,6,0),'Field Prep':(3,4,6),'Rewind Rounds':(3,6,6),'Triple Tap':(3,6,5),
 "Fourth Time's the Charm":(3,6,5),'Turnabout':(4,3,0),'Air Trigger':(4,3,0),'Steady Hands':(5,2,0),
 # --- PvE damage / interlocks ---
 'Kill Clip':(0,7,0),'Frenzy':(2,7,0),'Rampage':(0,6,0),'Bait and Switch':(0,9,0),'Envious Arsenal':(0,7,0),
 'Reservoir Burst':(0,7,0),'Explosive Light':(0,8,0),'Auto-Loading Holster':(0,6,5),'Heal Clip':(0,6,0),
 'Firefly':(0,7,0),'Incandescent':(0,8,0),'Voltshot':(0,8,0),'Destabilizing Rounds':(0,8,0),
 'Repulsor Brace':(0,7,0),'Demolitionist':(0,7,4),'Desperate Measures':(0,7,0),'Subsistence':(0,7,3),
 'Envious Assassin':(0,7,3),'Killing Tally':(0,7,0),'Lucky Shot':(0,7,0),'Shoot to Loot':(0,6,7),
 'Adhesive Ordnance':(0,6,0),'Headstone':(0,7,0),'Rimestealer':(0,6,0),'Crystalline Corpsebloom':(0,7,0),
 'Hatchling':(0,7,0),'Jolting Feedback':(0,7,0),'Chain Reaction':(0,8,0),'Explosive Payload':(1,5,0),
 'Timed Payload':(0,5,0),'Golden Tricorn':(0,8,0),'Strategist':(0,6,3),'One for All':(0,7,0),
 'Stats for All':(0,6,2),'Focused Fury':(0,7,0),'Overflow':(0,6,6),'Reconstruction':(0,8,7),
 'Surrounded':(0,6,0),'Swashbuckler':(0,6,0),'Multikill Clip':(0,6,0),'Adrenaline Junkie':(0,6,0),
 'Gutshot Straight':(0,6,0),'Recombination':(0,7,0),'Collective Action':(0,7,0),'Rolling Storm':(0,6,0),
 'Trickle Charge':(0,6,0),'Controlled Burst':(0,7,0),'Sympathetic Arsenal':(0,6,0),'Withering Gaze':(0,6,0),
 'Kinetic Tremors':(0,7,0),'Elemental Honing':(0,7,0),'Burning Ambition':(0,6,0),'Bewildering Burst':(0,6,0),
 'One-Two Punch':(0,7,0),'Vorpal Weapon':(0,6,0),'Unrelenting':(0,5,3),'Heating Up':(0,4,0),
 'Killing Wind':(0,3,2),'Feeding Frenzy':(0,6,0),'Outlaw':(0,6,0),'Grave Robber':(0,6,0),
 'Clown Cartridge':(0,6,3),'Cascade Point':(0,6,0),'Tear':(0,6,0),'Slice':(0,6,0),'Meganeura':(0,6,0),
 'Silkbound Slayer':(0,6,0),'Eddy Current':(0,6,0),'Shield Disorient':(1,5,0),'Thermal Atomization':(0,6,0),
 'Sword Logic':(0,6,0),'Eager Edge':(0,6,4),'Relentless Strikes':(0,6,0),'Whirlwind Blade':(0,7,0),
 'Tireless Blade':(0,6,0),"Assassin's Blade":(0,6,0),"Duelist's Trance":(0,7,0),'Valiant Charge':(0,6,0),
 'Shattering Blade':(0,6,0),'Lead from Gold':(0,5,7),'Wellspring':(0,6,5),'Permeability':(0,6,0),
 'Enlightened Action':(0,5,7),'Attrition Orbs':(0,6,8),'Dragonfly':(0,5,0),'Cluster Bomb':(0,6,0),
 'Bipod':(0,6,2),'Impulse Amplifier':(0,5,0),'Lasting Impression':(0,7,0),'Ambitious Assassin':(0,5,3),
 'Rapid Hit':(1,5,0),'Full Court':(0,6,0),'Tracking Module':(0,6,0),'Thresh':(0,5,4),
 'Physic':(0,5,8),'Reciprocity':(0,5,8),'Circle of Life':(0,5,8),'Parasitism':(0,7,0),'Transformative':(0,6,0),
 'Taken Ambition':(0,5,0),'Taken Divergence':(0,5,0),'Taken Resolution':(0,5,0),'Gear Shift':(0,6,0),
 'Discord':(0,5,0),'Reverberation':(0,6,0),'Detonator Beam':(0,6,0),'Proximity Power':(0,6,0),
 'Unstoppable Force':(0,6,0),'Immovable Object':(0,6,0),'Ancillary Ordinance':(0,6,3),'Aggregate Charge':(0,6,0),
 'Sneak Bow':(0,4,0),"Archer's Gambit":(0,6,0),"Archer's Tempo":(0,6,0),'Cold Steel':(0,6,0),
 'Offhand Strike':(0,5,0),'Melee Momentum':(0,5,0),'Collective Demolition':(0,6,0),'Collective Pugilism':(0,6,0),
 'Blast Distributor':(0,5,0),'Cooling Baubles':(0,5,0),'Supercharged Magazine':(0,5,0),'Paracausal Affinity':(0,5,0),
 'Kickstart':(0,5,3),'Loose Change':(0,5,3),'Perpetual Loophole':(0,6,0),'Replenishing Aegis':(0,5,3),
 'Bottomless Grief':(0,6,0),'Magnificent Howl':(0,7,0),'Firing Line':(0,7,0),'Nano-Assault':(0,6,0),
 'Mega Kill Clip':(0,6,0),'Successful Warm-Up':(0,5,0),'Butterfly':(0,6,0),'Explosive Head':(0,6,0),
 'Built to Blast':(0,6,0),'To the Pain':(1,5,0),'Desperado':(0,6,0),'Chaos Reshaped':(0,6,0),
 'Energy Transfer':(0,5,0),'Deconstruct':(0,6,0),'Temporal Anomaly':(0,6,0),'Transcendent Moment':(0,6,0),
 'En Garde':(0,5,0),'Invisible Hand':(0,6,0),'Mulligan':(0,4,4),'Backup Plan':(1,2,4),'Osmosis':(0,3,0),
 'Genesis':(0,5,3),'Adaptive Munitions':(0,5,3),'Shot Swap':(2,4,0),'Heart Piercer':(0,5,0),
 'Impromptu Ammunition':(0,4,6),'Bolt Scavenger':(0,4,7),'Lead From Light':(0,5,7),'Killing Tally':(0,7,0),
 'Light Touch':(0,4,0),'Hatchling':(0,7,0),'Pugilist':(4,4,0),'Iron Reach':(5,2,0),
 'Beacon Rounds':(0,5,0),'Tilting at Windmills':(0,5,0),'Fanatical Lance':(0,5,0),'Dimensional Shift':(0,5,0),
 'Danger Zone':(3,5,0),'Recycled Energy':(0,5,3),'Closing Time':(8,4,0),  # owner ruling 2026-10-25: top-tier PvP
'Threat Remover':(0,6,0),'Delicate Tuning':(0,4,0),
}
INTRINSIC_FRAMES = {'Aggressive Frame','Caster Frame','Lightweight Frame','Vortex Frame','Wave Sword Frame','Empty Traits Socket','Full Auto Trigger System'}

LANE = {'Hand Cannon','Scout Rifle','Pulse Rifle','Sniper Rifle','Combat Bow','Linear Fusion Rifle'}
SUSTAINED = {'Auto Rifle','Submachine Gun','Machine Gun','Trace Rifle','Sidearm'}
def pvp_val(trait, wtype):
    v = T.get(trait,(0,3,0))[0]
    if trait == 'Keep Away' and wtype not in LANE: return 0
    if trait in ('Target Lock','Dynamic Sway Reduction') and wtype not in SUSTAINED: return 0
    if wtype in ('Rocket Launcher','Sword','Glaive','Grenade Launcher','Machine Gun','Trace Rifle','Linear Fusion Rifle') and trait in ('Snapshot Sights','Opening Shot','Rangefinder'): return v-3
    return v

# PvE interlocks: bonus added to the pair (skill: interlocks beat raw numbers)
PVE_PAIRS = {
 frozenset(['Heal Clip','Kill Clip']):5, frozenset(['Envious Arsenal','Bait and Switch']):6,
 frozenset(['Envious Arsenal','Reservoir Burst']):5, frozenset(['Stats for All','One for All']):4,
 frozenset(['Auto-Loading Holster','Explosive Light']):5, frozenset(['Subsistence','Killing Tally']):4,
 frozenset(['Envious Assassin','Killing Tally']):4, frozenset(['Lucky Shot','Kill Clip']):4,
 frozenset(['Shoot to Loot','Adhesive Ordnance']):4, frozenset(['Demolitionist','Frenzy']):2,
 frozenset(['Reconstruction','Bait and Switch']):3, frozenset(['Firefly','Kill Clip']):2,
 frozenset(['Precision Instrument','Lucky Shot']):3, frozenset(['Reconstruction','Explosive Light']):3,
}

# ELEM: element of each elemental-verb trait; 2a chains get a bonus. Cure = solar, blind = arc.
ELEM = {
 'Incandescent':'solar','Burning Ambition':'solar','Heal Clip':'solar','Thermal Atomization':'solar',
 'Voltshot':'arc','Jolting Feedback':'arc','Collective Action':'arc','Rolling Storm':'arc','Eddy Current':'arc','Shield Disorient':'arc',
 'Destabilizing Rounds':'void','Repulsor Brace':'void','Demoralize':'void',
 'Headstone':'stasis','Crystalline Corpsebloom':'stasis','Rimestealer':'stasis','Chill Clip':'stasis',
 'Hatchling':'strand','Slice':'strand','Tear':'strand','Silkbound Slayer':'strand','Meganeura':'strand',
 'Elemental Honing':'any','Sympathetic Arsenal':'any','Elemental Capacitor':'any','Firefly':'solar',
}
CHAINS = [  # (applier, consumer) 2a, either column
 ('Destabilizing Rounds','Repulsor Brace'),('Demoralize','Repulsor Brace'),('Headstone','Rimestealer'),
 ('Crystalline Corpsebloom','Rimestealer'),('Incandescent','Burning Ambition'),('Rolling Storm','Trickle Charge'),
 ('Outlaw','Voltshot'),('Slideshot','Voltshot'),('Grave Robber','Voltshot'),('Clown Cartridge','Voltshot'),
 ('Jolting Feedback','Collective Action'),('Voltshot','Collective Action'),('Heal Clip','Firefly'),
]
CHAINSET = {frozenset(c) for c in CHAINS}

# ABTY: same-family pairs + generator->payoff
FAMILY = {
 'One-Two Punch':'melee','Trench Barrel':'melee','Pugilist':'melee','Melee Momentum':'melee','Offhand Strike':'melee',
 'Collective Pugilism':'melee','Close to Melee':'melee','Swashbuckler':'melee',
 'Demolitionist':'grenade','Desperate Measures':'grenade','Collective Demolition':'grenade','Ambitious Assassin':'grenade',
 'Strategist':'class','Golden Tricorn':'class','Wellspring':'gen','Permeability':'gen','Thresh':'super',
}
ABTY_PAIRS = {frozenset(['Strategist','Golden Tricorn']), frozenset(['Wellspring','Permeability']),
              frozenset(['Trench Barrel','One-Two Punch']), frozenset(['Demolitionist','Desperate Measures'])}

# Parts: stats that count as additive even when negative
NEG_GOOD = {'Charge Time','Draw Time'}
# Stats to judge deficiency by weapon class
DEFSTATS = ['Range','Stability','Handling','Reload Speed','Aim Assistance','Velocity','Blast Radius','Accuracy','Swing Speed','Guard Resistance','Charge Rate','Guard Endurance','Shield Duration']
BANNED_PARTS = {'Full Choke','Jagged Edge'}
