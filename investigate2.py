import json, os, collections

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

fusion = load("fusion.json")
fl = load("fusionlevel.json")
drops = load("drops.json")
droplists = load("droplists.json")
stages = load("stages.json")
monsters = load("monsters.json")
equip = load("equip.json")
weapons = load("weapons.json")
items = load("items.json")

print("=== FUSION rows (all 150, condensed: c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12 c13 c14) ===")
for f in fusion:
    print(" ".join(str(x) for x in f[:7]), "|", " ".join(str(x) for x in f[7:]))

print()
print("=== FUSIONLEVEL rows c0 c1 c2 c3 c4 c5 c6 (first 30) ===")
for r in fl[:30]:
    print(r)

print()
print("=== WEAPONS: ids existentes ===")
print("weapons ids:", [w[0] for w in weapons[:10]])
print()
print("=== EQUIP: ids por rango ===")
equip_ids = sorted(e["row"][0] for e in equip)
print("min/max:", equip_ids[0], equip_ids[-1], "count:", len(equip_ids))
print()

# drop: entender c4 y c1
print("=== DROPS: agrupando c1 (grupo?), mostrando items de cada grupo ===")
by_group = collections.defaultdict(list)
for d in drops:
    by_group[d[1]].append(d)
# c4 sample values - son droplist refs? o items?
c4s = [d[4] for d in drops]
print("sample c4:", c4s[:15])
print("c4 distinct count:", len(set(c4s)), "min:", min(c4s), "max:", max(c4s))

print()
print("=== DROPLISTS: c1 (grupo?), c6 (item?)? ===")
dl_by_group = collections.defaultdict(list)
for dl in droplists:
    dl_by_group[dl[1]].append(dl)
print("groups:", sorted(dl_by_group.keys())[:20])
print("group size distribution:", sorted(collections.Counter(len(v) for v in dl_by_group.values()).items())[:10])

print()
print("=== Droplists del grupo 1000100 ===")
for dl in droplists:
    if dl[1] == 1000100:
        print(dl)

print()
print("=== Stage -> monster refs c13, y monster c20/c21/c23/c24 ===")
for s in stages[:3]:
    print("stage", s[0], "c13(monsters):", s[13])
for m in monsters[:3]:
    print("monster", m[0], "c20:", m[20], "c21:", m[21], "c22:", m[22], "c23:", m[23], "c24:", m[24])

print()
print("=== droplist ids (c0) vs drop c1: coinciden? ===")
dl_ids = set(dl[0] for dl in droplists)
dl_c1 = set(dl[1] for dl in droplists)
drop_c1 = set(d[1] for d in drops)
drop_c4 = set(d[4] for d in drops)
print("droplist c0 in drop c1:", len(dl_ids & drop_c1))
print("droplist c1 in drop c1:", len(dl_c1 & drop_c1))
print("droplist c0 in drop c4:", len(dl_ids & drop_c4))
print("droplist c1 in drop c4:", len(dl_c1 & drop_c4))
print()

# es c10 = probability weight? cada droplist tiene c9/c10/c11
print("=== gachalist c5 vs equip/weapon/items ids ===")
gacha_item_ids = set(gl[5] for gl in load("gachalist.json"))
print("gachalist items que coinciden con equip:", len(gacha_item_ids & set(equip_ids)))
print("gachalist items que coinciden con weapons:", len(gacha_item_ids & set(w[0] for w in weapons)))
print("gachalist items que coinciden con items:", len(gacha_item_ids & set(i["row"][0] for i in items)))
print()

# droplist c6 coincide con equip/weapon/items?
dl_item_ids = set(dl[6] for dl in droplists)
print("droplist c6 con equip:", len(dl_item_ids & set(equip_ids)))
print("droplist c6 con weapons:", len(dl_item_ids & set(w[0] for w in weapons)))
print("droplist c6 con items:", len(dl_item_ids & set(i["row"][0] for i in items)))