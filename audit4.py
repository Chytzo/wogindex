import json, os

p = os.path.expanduser("~/Proyectos/wog-wiki/data/resolved_tables.json")
with open(p, encoding="utf-8") as fh:
    data = json.load(fh)

for tbl in ["fusion", "fusionlevel", "drop", "droplist", "gacha", "gachalist", "item", "hero", "equip"]:
    rows = data[tbl]["rows"]
    print("==", tbl, "len", len(rows), "row0 type:", type(rows[0]).__name__)
    print("   row0:", json.dumps(rows[0], ensure_ascii=False)[:500])
    print("   row1:", json.dumps(rows[1], ensure_ascii=False)[:300] if len(rows) > 1 else "")
    print()