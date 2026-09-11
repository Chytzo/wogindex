#!/usr/bin/env python3
"""Aplica base a hrefs usando import.meta.env.BASE_URL INLINE (sin const base en frontmatter).
El compilador de Astro tiene un bug: `const base = import.meta.env.BASE_URL;` en frontmatter
se manglea a `import.meta.env.BAS\nastro';`. Usar inline en el body evita el bug."""
import os, glob, re

ROOT = os.path.expanduser("~/Proyectos/wog-wiki/src")
files = glob.glob(os.path.join(ROOT, "layouts", "*.astro")) + glob.glob(os.path.join(ROOT, "pages", "**", "*.astro"), recursive=True)

for fp in sorted(files):
    with open(fp, "r", encoding="utf-8") as f:
        s = f.read()
    orig = s

    # 1) quitar cualquier `const base = import.meta.env.BASE_URL;` del frontmatter
    s = s.replace("const base = import.meta.env.BASE_URL;\n", "")

    # 2) hrefs dinámicos ya convertidos: href={`${base}x`} -> href={`${import.meta.env.BASE_URL}x`}
    s = s.replace('href={`${base}', 'href={`${import.meta.env.BASE_URL}')

    # 2b) hrefs dinámicos originales con barra literal: href={`/heroes/..`} -> href={`${import.meta.env.BASE_URL}heroes/..`}
    s = s.replace('href={`/', 'href={`${import.meta.env.BASE_URL}')

    # 3) hrefs estáticos href="/x" -> href={`${import.meta.env.BASE_URL}x`}
    def fstat(m):
        return 'href={`${import.meta.env.BASE_URL}' + m.group(1) + '`}'
    s = re.sub(r'href="/([^"]*)"', fstat, s)

    s = s.replace('href={`${import.meta.env.BASE_URL}`}/', 'href={`${import.meta.env.BASE_URL}`}')
    s = s.replace('href={`${import.meta.env.BASE_URL}/`}', 'href={`${import.meta.env.BASE_URL}`}')

    if s != orig:
        open(fp, "w", encoding="utf-8").write(s)
        print("fixed:", os.path.relpath(fp, ROOT))
    else:
        print("skip :", os.path.relpath(fp, ROOT))