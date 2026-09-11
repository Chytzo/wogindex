#!/usr/bin/env python3
import os, subprocess, sys

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print("$", cmd)
    out = (r.stdout or "").strip()
    err = (r.stderr or "").strip()
    if out: print(out)
    if err: print("ERR:", err)
    return r.returncode

os.chdir(os.path.expanduser("~/Proyectos/wog-wiki"))

# 1. .gitignore real
with open(".gitignore", "w") as f:
    f.write("node_modules/\nbuild.log\n")
print(".gitignore written")

# 2. ensure dist exists (build output)
run("git add -A")
run('git -c user.email="wogindex-bot@chytzo.dev" -c user.name="WoG Index Bot" commit -m "gitignore fix" --allow-empty')

# 3. push
run("git push -u origin main")