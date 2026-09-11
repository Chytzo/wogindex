import json, os, collections

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

drops = load("drops.json")
droplists = load("droplists.json")
stages = load("stages.json")
monsters = load("monsters.json")
equip = load("equip.json")
items = load("items.json")
weapons = load("weapons.json")
gacha = load("gacha.json")
gachalist = load("gachalist.json")

# 1) En qué columna del stage aparece drop.c1?
drop_c1 = set(d[1] for d in drops)
for ci in range(len(stages[0])):
    vals = set()
    for s in stages:
        v = s[ci]
        if isinstance(v, int):
            vals.add(v)
        elif isinstance(v, list):
            for x in v:
                if isinstance(x, int):
                    vals.add(x)
    inter = vals & drop_c1
    if inter:
        print(f"stage c{ci}: {len(inter)} matches, sample {sorted(inter)[:8]}")

print()
# 2) droplist c2 meanings: 1,2,3,5 -> ver IDs de grupo
print("droplist groups sample:", sorted(set(dl[1] for dl in droplists))[:10])
print("droplist c2==5 sample group:", [dl for dl in droplists if dl[2]==5][:3])
print("droplist c2==1 sample group:", [dl for dl in droplists if dl[2]==1][:3])
print()
# group by (c1, c2)
for c2 in sorted(set(dl[2] for dl in droplists)):
    groups = set(dl[1] for dl in droplists if dl[2]==c2)
    print(f"c2={c2}: {len(groups)} groups, sample {sorted(groups)[:8]}")

print()
# 3) relación gacha vs gachalist: gacha.c? y gachalist.c2?
print("gacha sample:", gacha[0])
print("gachalist sample:", gachalist[0])
gacha_c1 = set(g[1] for g in gacha)
gl_c2 = set(gl[2] for gl in gachalist)
print("gacha.c1 set sample:", sorted(gacha_c1)[:10])
print("gachalist c2 values:", sorted(gl_c2))

# ¿gachalist.c? == gacha.c0?
gl_gacha_ref = collections.Counter()
for gl in gachalist[:20]:
    print("gachalist:", gl)

# 4) drop: relación c1 (100100) -> c4 (1000100)? multiple c4 por c1?
print()
c1_to_c4 = collections.defaultdict(set)
for d in drops:
    c1_to_c4[d[1]].add(d[4])
for c1 in sorted(c1_to_c4)[:5]:
    print(f"drop.c1={c1} -> c4={sorted(c1_to_c4[c1])}")
print("total c1:", len(c1_to_c4), "c4:", len(set(d[4] for d in drops)))

# 5) droplist: c1 is group (1000100). Quien referencia droplist.c1=1000100? drop.c4.
#    droplist.c9/c10/c11? pesos
print()
print("droplist c7/c8 distinct:", sorted(set(dl[7] for dl in droplists)), sorted(set(dl[8] for dl in droplists)))
print("droplist c9 distinct:", sorted(set(dl[9] for dl in droplists)))
print("droplist c10 distinct:", sorted(set(dl[10] for dl in droplists)))
print("c11 distinct max:", max(dl[11] for dl in droplists))