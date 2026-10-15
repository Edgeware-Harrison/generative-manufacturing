# One-off live check of every external source URL (needs network). Not part of validate.py.
import json, subprocess
bad=False
BOT_BLOCKED={"autodesk":"403 to curl (bot protection); page content verified with a browser-style fetch on 2026-10-15"}
for k,u in json.load(open("sources.json"))["sources"].items():
    r=subprocess.run(["curl","-s","-L","-m","25","-A","Mozilla/5.0","-o","/dev/null","-w","%{http_code} %{url_effective}",u],capture_output=True,text=True)
    out=r.stdout.strip() or r.stderr.strip()
    if not out.startswith("200") and k in BOT_BLOCKED: out="OK* "+out+" ["+BOT_BLOCKED[k]+"]"
    elif not out.startswith("200"): bad=True
    print(k,out)
import sys; sys.exit(1 if bad else 0)
