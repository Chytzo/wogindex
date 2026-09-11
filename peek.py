import os, sys
fp = os.path.expanduser("~/Proyectos/wog-wiki/src/pages/gacha.astro")
lines = open(fp, encoding="utf-8").read().split("\n")
for i, l in enumerate(lines, 1):
    if 24 <= i <= 32 or "href" in l or "${" in l:
        print(f"{i}: {l}")