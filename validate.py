import json, glob, re
from html.parser import HTMLParser
DEF="Generative Manufacturing (GenM) is the manufacturing paradigm in which AI compiles human intent into fulfillable physical outcomes, so the demand side speaks in intent and verified engineering paths make good on it."
VOID={"meta","link","br","img","input","hr"}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st or s.st[-1]!=t: s.err.append(f"mismatch </{t}> stack={s.st[-3:]}")
        else: s.st.pop()
ok=True
for f in sorted(glob.glob("**/*.html",recursive=True)):
    h=open(f).read(); p=P(); p.feed(h)
    if p.st or p.err: ok=False; print("HTML FAIL",f,p.err,p.st)
    blocks=re.findall(r'<script type="application/ld\+json">(.*?)</script>',h,re.S)
    for b in blocks: json.loads(b)
    if DEF not in h: ok=False; print("DEF missing",f)
    if re.search(r'15 years[^.]{0,80}(factory|ODM|Surabaya)',h): ok=False; print("GUARDRAIL",f)
    print("ok",f,len(blocks),"JSON-LD")
for f in glob.glob("schema/*.jsonld"): json.loads(open(f).read()); print("ok",f)
import xml.dom.minidom; xml.dom.minidom.parse("sitemap.xml"); print("ok sitemap.xml")
BASE="https://whatisgenm.com"
import os
for f in glob.glob("**/*",recursive=True):
    if os.path.isfile(f) and f not in ("validate.py","build.py","README.md","CNAME"):
        t=open(f,encoding="utf-8").read()
        if "YOUR-GH" in t or "genm-site" in t or "github.io" in t: ok=False; print("OLD BASE",f)
        if "hreflang" in t or BASE+"/zh" in t: ok=False; print("ZH REF",f)
for f in ("README.md","build.py"):
    t=open(f).read()
    if f=="README.md": t=re.sub(r"<!-- DNS-NOTES-START -->.*?<!-- DNS-NOTES-END -->","",t,flags=re.S)
    if "github.io" in t: ok=False; print("github.io outside DNS notes",f)
if open("CNAME").read()!="whatisgenm.com": ok=False; print("CNAME bad")
if os.path.exists("zh"): ok=False; print("zh/ exists")
faq=json.load(open("schema/faqpage.jsonld"))
assert faq["@type"]=="FAQPage" and all(q["acceptedAnswer"]["text"] for q in faq["mainEntity"])
assert faq["mainEntity"][0]["acceptedAnswer"]["text"]==DEF
p=json.load(open("schema/person.jsonld")); assert "https://github.com/Edgeware-Harrison" in p["sameAs"]
locs=re.findall(r"<loc>(.*?)</loc>",open("sitemap.xml").read())
for u in locs:
    path=u[len(BASE)+1:]; fp=(path+"index.html") if (path=="" or path.endswith("/")) else path
    if not os.path.exists(fp): ok=False; print("SITEMAP MISSING",u)
for u in re.findall(r"\((https://edgeware[^)]*)\)",open("llms.txt").read()):
    path=u[len(BASE)+1:]; fp=(path+"index.html") if (path=="" or path.endswith("/")) else path
    if not os.path.exists(fp): ok=False; print("LLMS MISSING",u)
if DEF not in open("llms-full.txt").read(): ok=False
print("sitemap urls",len(locs))
print("ALL PASS" if ok else "FAILURES")
