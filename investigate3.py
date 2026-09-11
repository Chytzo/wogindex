import json, os, collections

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

drops = load("drops.json")
droplists = load("droplists.json")
stages = load("stages.json")
monsters = load("monsters.json")
gacha = load("gacha.json")
gachalist = load("gachalist.json")

# decode weapons
try:
    weapons = load("weapons.json")
    if weapons and isinstance(weapons[0], dict):
        print("weapons[0]:", json.dumps(weapons[0], ensure_ascii=False)[:300])
        print("weapons ids:", [w["row"][0] for w in weapons[:5]])
    else:
        print("weapons[0]:", json.dumps(weapons[0], ensure_ascii=False)[:200])
except Exception as e:
    print("weapons err:", e)

print()
# drop c1 domain: what references exist? monsters? stages? gacha?
monster_ids = set(m[0] for m in monsters)
stage_ids = set(s[0] for s in stages)
gacha_ids = set(g[0] for g in gacha)
dl_ids = set(dl[0] for dl in droplists)
dl_groups = set(dl[1] for dl in droplists)

drop_c1 = set(d[1] for d in drops)
drop_c4 = set(d[4] for d in drops)

print("drop c1 ∩ monster:", len(drop_c1 & monster_ids))
print("drop c1 ∩ stage:", len(drop_c1 & stage_ids))
print("drop c1 ∩ gacha:", len(drop_c1 & gacha_ids))
print("drop c1 ∩ droplist c0:", len(drop_c1 & dl_ids))
print("drop c1 ∩ droplist c1:", len(drop_c1 & dl_groups))
print("drop c4 ∩ monster:", len(drop_c4 & monster_ids))
print("drop c4 ∩ stage:", len(drop_c4 & stage_ids))
print("drop c4 ∩ gacha:", len(drop_c4 & gacha_ids))
print("drop c4 ∩ droplist c0:", len(drop_c4 & dl_ids))
print("drop c4 ∩ droplist c1:", len(drop_c4 & dl_groups))

print()
print("sample drop c1 values:", sorted(drop_c1)[:30])
print("sample drop c4 values:", sorted(drop_c4)[:30])

print()
# monster other cols
print("=== monster cols c20-c27 ===")
mmon = set()
for m in monsters:
    for c in (18, 19, 20, 21, 22, 23, 24, 25, 26, 27):
        v = m[c]
        if isinstance(v, list):
            mmon |= set(v)
        elif isinstance(v, int) and v > 0:
            mmon.add(v)
print("monster ref ids heads:", sorted(mmon)[:40])
print("monster refs ∩ drop c1:", len(mmon & drop_c1))
print("monster refs ∩ droplist c0:", len(mmon & dl_ids))
print("monster refs ∩ droplist c1:", len(mmon & dl_groups))

print()
# stage cols
sm = set()
for s in stages:
    for c in range(8, 40):
        v = s[c]
        if isinstance(v, list):
            sm |= set(v)
        elif isinstance(v, int) and v > 0:
            sm.add(v)
print("stage ref IDs (subset):", sorted(sm)[:50])
print("stage refs ∩ droplist c0:", len(sm & dl_ids))
print("stage refs ∩ droplist c1:", len(sm & dl_groups))
print("stage refs ∩ drop c1:", len(sm & drop_c1))
print("stage refs ∩ drop c4:", len(sm & drop_c4))

print()
# droplist c2 groups: 1,2,3,5
print("=== droplist by c2 (type) counts ===")
print(collections.Counter(dl[2] for dl in droplists))
print()
# gacha c2?
print("gacha col c1?", collections.Counter(g[1] for g in gacha).most_common(5))
print("gacha c12/c11:", gacha[0][11], gacha[0][12])
print()
# where do gacha pools get referenced?
print("gachalist c1 = gacha c0?", len(set(gl[1] for gl in gachalist) & gacha_ids), "of", len(gacha_ids))