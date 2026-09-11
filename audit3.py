import json, os

p = os.path.expanduser("~/Proyectos/wog-wiki/data/resolved_tables.json")
with open(p, encoding="utf-8") as fh:
    data = json.load(fh)

for tbl in ["fusion", "fusionlevel", "drop", "droplist", "gacha", "gachalist", "item", "hero", "equip"]:
    d = data[tbl]
    print(tbl, "-> keys:", list(d.keys()))
    inner = d.get("data") if "data" in d else d.get("rows") if "rows" in d else None
    if inner is None:
        for k, v in d.items():
            if k == "file":
                continue
            print("   other key:", k, "type:", type(v).__name__)
            if isinstance(v, str):
                print("   value head:", v[:300])
            elif isinstance(v, (list, dict)):
                print("   head:", json.dumps(v, ensure_ascii=False)[:400])
        print()
        continue
    print("   inner type:", type(inner).__name__, "len:", len(inner))
    if isinstance(inner, list) and inner and isinstance(inner[0], dict):
        print("   row0 keys:", list(inner[0].keys()))
        print("   row0:", json.dumps(inner[0], ensure_ascii=False)[:400])
    elif isinstance(inner, dict):
        k0 = next(iter(inner))
        print("   key0:", k0, "->", json.dumps(inner[k0], ensure_ascii=False)[:300])
    print()