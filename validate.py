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

# ================= release checks (added for the staged release) =================
import sys
from html.parser import HTMLParser as _HP
SOURCES=json.load(open("sources.json"))["sources"]
class L(_HP):
    def __init__(s): super().__init__(); s.links=[]; s.skip=0; s.text=[]
    def handle_starttag(s,t,a):
        d=dict(a)
        if t=="a" and "href" in d: s.links.append(d["href"])
        if t in ("script","style"): s.skip+=1
    def handle_endtag(s,t):
        if t in ("script","style"): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.text.append(d)
def fail(*a):
    global ok; ok=False; print("FAIL",*a)
def exists(url):
    path=url[len(BASE):].split("#")[0].lstrip("/")
    return os.path.exists((path+"index.html") if (path=="" or path.endswith("/")) else path)
pages=sorted(glob.glob("**/index.html",recursive=True))
NOINDEX={"essays/index.html"}
defined={}; refs=[]
def walk(o,pg):
    if isinstance(o,dict):
        if "@id" in o:
            (refs.append((o["@id"],pg)) if len(o)==1 else defined.__setitem__(o["@id"],pg))
        for x in o.values(): walk(x,pg)
    elif isinstance(o,list):
        for x in o: walk(x,pg)
ext=set()
html_of={}
for f in pages:
    h=open(f).read(); html_of[f]=h; lp=L(); lp.feed(h); slug=os.path.dirname(f); url=f"{BASE}/{slug}/" if slug else f"{BASE}/"
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',h,re.S): walk(json.loads(b),f)
    if f'<link rel="canonical" href="{url}">' not in h: fail("canonical",f)
    has_ni='name="robots" content="noindex' in h
    if (f in NOINDEX)!=has_ni: fail("noindex wrong (only essays may be noindex)",f,has_ni)
    if 'draftbanner' in h or "DRAFT: not published" in h: fail("draft banner left",f)
    if "<nav aria-label=\"Primary\">" not in h: fail("new nav missing",f)
    for need in ("/glossary/","/genm-vs-adjacent-terms/","/timeline/","/essays/","/faq/","/what-is-genm/"):
        if f"{BASE}{need}" not in h.split("<main>")[0]: fail("nav link missing",f,need)
    if re.search(r"\bcoined\b|\bI invented\b",h): fail("coinage claim",f)
    if re.search(r"Edgeware[^.<]{0,100}(deliver|pilot|customer|deployed|shipped|orders)",h,re.I): fail("Edgeware claim",f)
    if "Surabaya" in h and "2010" not in h: fail("Surabaya without dates",f)
    if re.search(r"15 years[^.<]{0,80}(factory|ODM|Surabaya)|(factory|ODM|Surabaya)[^.<]{0,80}15 years",h): fail("15-years",f)
    if "{" in "".join(lp.text) or "TODO" in h: fail("leftover braces/TODO",f)
    for l in lp.links:
        if l.startswith(BASE):
            if not exists(l): fail("broken internal link",f,l)
        elif l.startswith("http"): ext.add(l)
        else: fail("non-absolute link",f,l)
for i,pg in refs:
    if i not in defined: fail("unresolved @id",i,pg)
bad=[u for u in ext if u not in SOURCES.values() and u not in ("https://x.com/HarrisonCc1004","https://www.linkedin.com/in/harrisonchan-genm")]
if bad: fail("external links not in sources.json",bad)
# decisions
if "my name for" in html_of["index.html"] or "my definition of the shift" not in html_of["index.html"]: fail("home wording")
d=html_of["distinctions/index.html"]
for need in ["I did not invent the words","engineering.cmu.edu/mfi/research/generative-manufacturing.html","arxiv.org/abs/2409.03089","cloudnc.com/blog/generative-manufacturing-or-how-to-transform-how-we-make-everything-forever","16 October 2024","4 September 2024","/genm-vs-adjacent-terms/","What this page is for"]:
    if need not in d: fail("distinctions missing",need)
if "/zh/" in d: fail("distinctions links zh CloudNC URL")
c=html_of["genm-vs-adjacent-terms/index.html"]
for need in ["/distinctions/","What this page is for"]:
    if need not in c: fail("compare missing",need)
t=html_of["timeline/index.html"]
rows=[r for r in re.findall(r"<tr[^>]*>(.*?)</tr>",t,re.S)[1:]]
auth=[r for r in rows if "author-stated" in re.findall(r"<td>(.*?)</td>",r,re.S)[-1]]
if len(auth)!=3: fail("timeline must have exactly 3 author-stated rows, found",len(auth))
atxt=" ".join(auth)
for need in ["Surabaya","2010 to 2020","Miracle Plus Physical AI Lab","Edgeware","c. 2021"]:
    if need not in atxt: fail("author-stated row missing",need)
if "Arterki" in t or "Taktak" in t: fail("Arterki/Taktak must stay off the timeline")
if "15 years" in t: fail("15 years on timeline")
for r in rows:
    cells=re.findall(r"<td>(.*?)</td>",r,re.S)
    if len(cells)!=4 or not all(x.strip() for x in cells): fail("timeline row incomplete",r[:50])
if "Surabaya" in t and ("company" not in t or "not disclosed" not in t): fail("Surabaya row must say name not disclosed")
# glossary set id aligned with live term pages
gs=json.load(open("schema/definedtermset.jsonld")) if os.path.exists("schema/definedtermset.jsonld") else None
if not gs or gs["@id"]!=f"{BASE}/#glossary": fail("DefinedTermSet @id must be",f"{BASE}/#glossary")
tm=json.load(open("schema/definedterm.jsonld"))
if tm["inDefinedTermSet"]["@id"]!=gs["@id"]: fail("term/termset id mismatch")
# sitemap / llms
locs=re.findall(r"<loc>(.*?)</loc>",open("sitemap.xml").read())
for p in ("glossary/","genm-vs-adjacent-terms/","timeline/","distinctions/"):
    if f"{BASE}/{p}" not in locs: fail("sitemap missing",p)
if f"{BASE}/essays/" in locs: fail("noindex essays must not be in sitemap")
ll=open("llms.txt").read(); lf=open("llms-full.txt").read()
for p in ("glossary/","genm-vs-adjacent-terms/","timeline/","distinctions/"):
    if f"{BASE}/{p}" not in ll: fail("llms.txt missing",p)
    if f"URL: {BASE}/{p}" not in lf: fail("llms-full.txt missing",p)
if "/essays/" in ll or "URL: "+BASE+"/essays/" in lf: fail("essays must not be in llms files")
for u in re.findall(r"\((https://whatisgenm[^)]*)\)",ll):
    if not exists(u): fail("llms.txt dead link",u)
for f in pages:
    target=f"{BASE}/{os.path.dirname(f)}/" if os.path.dirname(f) else f"{BASE}/"
    if not any(target in html_of[g] for g in pages if g!=f): fail("orphan",f)
print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
