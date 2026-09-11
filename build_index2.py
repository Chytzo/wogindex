import json, os, collections

base = os.path.expanduser("~/Proyectos/wog-wiki/src/data")

def load(name):
    with open(os.path.join(base, name), encoding="utf-8") as fh:
        return json.load(fh)

def dump(name, obj):
    with open(os.path.join(base, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
    print("wrote", name)

d = load("dropfinder.json")

# filter: drop unnamed (#NNN only)
clean = {}
for iid, v in d.items():
    nm = v["name"]
    if nm == f"#{iid}" or not nm:
        continue
    # dedupe sources by (stage, kind): keep best rate
    bykey = {}
    for s in v["sources"]:
        k = (s["stage"], s["kind"])
        if k not in bykey or s["rate"] > bykey[k]["rate"]:
            bykey[k] = s
    sorted_srcs = sorted(bykey.values(), key=lambda x: (-x["rate"], x["stage"]))
    clean[str(iid)] = {"name": nm, "sources": sorted_srcs}

print("clean items:", len(clean))
total_src = sum(len(v["sources"]) for v in clean.values())
print("total sources after dedupe:", total_src)

# stats for show
for iid in ("201001", "201002"):
    if iid in clean:
        v = clean[iid]
        print(f"{iid} {v['name']}: {len(v['sources'])} sources")

# sort index by name
idx = sorted(
    [{"id": iid, "name": v["name"], "n": len(v["sources"]),
      "best": min((s["rate"] for s in v["sources"]), default=0)} for iid, v in clean.items()],
    key=lambda x: x["name"].lower(),
)

size_est = sum(len(json.dumps(v, ensure_ascii=False)) for v in clean.values())
print("full clean JSON approx size:", round(size_est/1024/1024, 2), "MB")
idx_size = len(json.dumps(idx, ensure_ascii=False))
print("index approx size:", round(idx_size/1024, 1), "KB")

dump("dropfinder_index.json", idx)
dump("dropfinder_min.json", clean)