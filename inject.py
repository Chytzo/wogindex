import os
fp = os.path.expanduser("~/Proyectos/wog-wiki/src/pages/fusion.astro")
s = open(fp, encoding="utf-8").read()
s = s.replace("---\n", "---\nconst base = import.meta.env.BASE_URL;\n", 1)
open(fp, "w", encoding="utf-8").write(s)
print("injectado en fusion.astro")