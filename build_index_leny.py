import json, os

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")
p = os.path.join(base, "dropfinder.json")
size = os.path.getsize(p)
print("dropfinder.json size:", size, "bytes =", round(size/1024/1024, 2), "MB")

d = json.load(open(p, encoding="utf-8"))
idx = []
for iid, v in d.items():
    srcs = v["sources"]
    idx.append({
        "id": iid,
        "name": v["name"],
        "n": len(srcs),
        "stages": len({s["stage"] for s in srcs}),
        "best": min((s["rate"] for s in srcs), default=0),
    })
idx.sort(key=lambda x: x["name"].lower())
with open(os.path.join(base, "dropfinder_index.json"), "w", encoding="utf-8") as fh:
    json.dump(idx, fh, ensure_ascii=False)
print("wrote dropfinder_index.json:", len(idx), "entries")
print("sample:")
for e in idx[:5]:
    print("  ", e)

# total unique stages with a name
stages_all = json.load(open(os.path.join(base, "stages.json"), encoding="utf-8"))
print("total stages:", len(stages_all))