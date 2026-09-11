#!/usr/bin/env python3
import os, subprocess, shutil

def run(cmd, chdir=None):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=chdir)
    out = (r.stdout or "").strip()
    err = (r.stderr or "").strip()
    if out: print(f"$ {cmd}\n{out}")
    if err and r.returncode != 0: print(f"ERR: {err}")
    return r.returncode

REPO = os.path.expanduser("~/Proyectos/wog-wiki")
os.chdir(REPO)

# 1. commit dist to main (so history has it)
run("git rm -r --cached dist >/dev/null 2>&1")
run("git add -A; git add -f dist public")
run('git -c user.email="wogindex@chytzo.dev" -c user.name="WoG Index Bot" commit -m "data: update - resolved names" --allow-empty')
run("git push origin main")

# 2. rebuild gh-pages from ORIGIN main dist (fresh clone to avoid wrecking local)
CLONE = "/tmp/wog-deploy"
if os.path.exists(CLONE): shutil.rmtree(CLONE)
os.makedirs(CLONE)
run("git clone --depth 1 --branch main https://github.com/Chytzo/wogindex.git .", chdir=CLONE)
std = os.path.join(CLONE, "dist")
dstd = os.path.join(CLONE, "dist2")
if os.path.exists(dstd): shutil.rmtree(dstd)
shutil.copytree(std, dstd)

run("git checkout --orphan gh-pages2", chdir=CLONE)
run("git rm -rf --cached . >/dev/null 2>&1", chdir=CLONE)
for item in os.listdir(CLONE):
    if item.startswith(".git"): continue
    p = os.path.join(CLONE, item)
    if os.path.isdir(p): shutil.rmtree(p)
    else: os.unlink(p)
for item in os.listdir(dstd):
    shutil.move(os.path.join(dstd, item), os.path.join(CLONE, item))
shutil.rmtree(dstd, ignore_errors=True)
open(os.path.join(CLONE, ".nojekyll"), "w").close()

run('git -c user.email="wogindex@chytzo.dev" -c user.name="WoG Index Bot" add -A', chdir=CLONE)
run('git -c user.email="wogindex@chytzo.dev" -c user.name="WoG Index Bot" commit -m "deploy" --allow-empty', chdir=CLONE)
run("git branch -M gh-pages", chdir=CLONE)
run("git push -f origin gh-pages", chdir=CLONE)

print("DEPLOYED")