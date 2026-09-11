#!/usr/bin/env python3
import os, subprocess

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        print("ERR:", r.stderr.strip())
        raise SystemExit(r.returncode)

os.chdir(os.path.expanduser("~/Proyectos/wog-wiki"))
run('git add -A')
run('git -c user.email="wogindex@chytzo.dev" -c user.name="WoG Index Bot" commit -m "deploy: rebuild dist with base-prefixed links"')
run("git push origin main")
print("COMMITTED+PUSHED")