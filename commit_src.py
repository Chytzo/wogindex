#!/usr/bin/env python3
import os, subprocess

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        print("ERR:", r.stderr.strip())
        raise SystemExit(r.returncode)

os.chdir(os.path.expanduser("~/Proyectos/wog-wiki"))
run('git add -A src astro.config.mjs fix_base.py')
run('git -c user.email="wogindex@chytzo.dev" -c user.name="WoG Index Bot" commit -m "fix: use inline import.meta.env.BASE_URL for links - const base broke Astro compiler"')
run("git push origin main")
print("COMMITTED+PUSHED")