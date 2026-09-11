import json, os, collections

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

drops = load("drops.json")
droplists = load("droplists.json")
gacha = load("gacha.json")
gachalist = load("gachalist.json")
stages = load("stages.json")
monsters = load("monsters.json")
equip = load("equip.json")
items = load("items.json")

def item_name(num):
    for src in (items, equip):
        if isinstance(src[0], dict):
            e = src.find(lambda x: x["row"][0] == num) if False else next((x for x in src if x["row"][0] == num), None)
            if e:
                return e.get("name_en") or e.get("name_es") or f"#{num}"
    return f"#{num}"

print("=== STAGES structure (first row) ===")
print(json.dumps(stages[0], ensure_ascii=False)[:600])
print()
print("=== MONSTERS structure (first row) ===")
print(json.dumps(monsters[0], ensure_ascii=False)[:600])
print()
# distinct drop item ids
print("=== drops: distinct item references (c4) ===")
c4s = collections.Counter(d[4] for d in drops)
print("distinct c4:", len(c4s))
print("=== drops: c1 (group?) distinct sample ===")
print("c1 min/max:", min(d[1] for d in drops), max(d[1] for d in drops))
print("=== drops: c10 max ===", max(d[10] for d in drops))
print("=== drops sample rows with c4 items names ===")
# show drop rows where c4 matches an equip/item id
ids_items = {e["row"][0] for e in equip} | {e["row"][0] for e in items}
seen = 0
for d in drops:
    if d[4] in ids_items:
        print("drop:", d, "->", item_name(d[4]))
        seen += 1
        if seen >= 10:
            break
print()
print("=== droplists: c1 distinct? c2? c6? c9? c10? c11? ===")
print("c1 min/max:", min(d[1] for d in droplists), max(d[1] for d in droplists))
print("c2 distinct:", sorted(set(d[2] for d in droplists)))
print("c6 distinct ids (items):", len(set(d[6] for d in droplists)))
print("c9 distinct:", sorted(set(d[9] for d in droplists)))
print("c9 min/max:", min(d[9] for d in droplists), max(d[9] for d in droplists))
print("c10 distinct:", sorted(set(d[10] for d in droplists)), "c11 max:", max(d[11] for d in droplists))
print("sample droplists of item 201001 (Iron Sword):")
for d in droplists:
    if d[6] == 201001:
        print("  ", d)
print()
print("=== gacha: c4? ===")
print("gacha c4 distinct:", len(set(g[4] for g in gacha)))
print("gacha sample:", gacha[0])
print("=== gachalist: c5 (item?) ===")
print("gachalist c5 distinct:", len(set(g[5] for g in gachalist)))
print("gachalist sample:", gachalist[0])