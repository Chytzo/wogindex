import json, os, sys

data_dir = os.path.expanduser("~/Proyectos/wog-wiki/data")
if not os.path.isdir(data_dir):
    print("NO DATA DIR:", data_dir)
    sys.exit(0)

for f in sorted(os.listdir(data_dir)):
    p = os.path.join(data_dir, f)
    try:
        with open(p, encoding="utf-8") as fh:
            d = json.load(fh)
        if isinstance(d, list):
            n = len(d)
            shape = f"list[{n}]"
            if n and isinstance(d[0], dict):
                keys = list(d[0].keys())
                shape += f" keys={keys[:25]}"
        elif isinstance(d, dict):
            shape = f"dict keys={list(d.keys())[:25]}"
        else:
            shape = type(d).__name__
        print(f"{f}: {shape}")
    except Exception as e:
        print(f"{f}: ERROR {e}")