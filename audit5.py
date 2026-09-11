import json, os, glob

src = os.path.expanduser("~/Proyectos/wog-wiki/src/data")
for f in sorted(glob.glob(src + "/*.json")):
    name = os.path.basename(f)
    with open(f, encoding="utf-8") as fh:
        d = json.load(fh)
    print(f"{name}: {len(d)} items")
    if d:
        first = d[0]
        if isinstance(first, dict):
            print("  sample keys:", list(first.keys()))
            if "row" in first:
                print("  row len:", len(first["row"]))
                print("  sample:", json.dumps(first, ensure_ascii=False)[:300])
            else:
                print("  sample:", json.dumps(first, ensure_ascii=False)[:300])
        else:
            print("  sample:", json.dumps(first, ensure_ascii=False)[:200])
    print()