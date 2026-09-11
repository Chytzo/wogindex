import os, glob, re
from collections import Counter

files = glob.glob(os.path.expanduser("~/Proyectos/wog-wiki/src/pages/**/*.astro"), recursive=True)
files += glob.glob(os.path.expanduser("~/Proyectos/wog-wiki/src/layouts/*.astro"))
c = Counter()
for fp in files:
    s = open(fp, encoding="utf-8").read()
for m in re.findall(r"text-gray-[\w/%-]+", s):
    c[m] += 1
for k, v in c.most_common(30):
    print(f"{v:4} {k}")