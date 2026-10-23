import json, os, html
BASE="https://whatisgenm.com"
DEF="Generative Manufacturing (GenM) is the manufacturing paradigm in which AI compiles human intent into fulfillable physical outcomes, so the demand side speaks in intent and verified engineering paths make good on it."
P1_SLUG="why-no-one-has-a-compiler-for-physical-things-yet"
P2_SLUG="intent-not-drawings"
BIO="Harrison Chan, founder of Edgeware, defining Generative Manufacturing (GenM)."
person={"@context":"https://schema.org","@type":"Person","@id":f"{BASE}/#person","name":"Harrison Chan","description":BIO,
 "jobTitle":"Founder","worksFor":{"@type":"Organization","name":"Edgeware"},
 "knowsAbout":["Generative Manufacturing","Physical AI","Overseas manufacturing"],
 "url":f"{BASE}/","sameAs":["https://x.com/HarrisonCc1004","https://www.linkedin.com/in/harrisonchan-genm","https://github.com/Edgeware-Harrison"]}
term={"@context":"https://schema.org","@type":"DefinedTerm","@id":f"{BASE}/what-is-genm/#term","name":"Generative Manufacturing",
 "alternateName":["GenM","生成式制造"],"description":DEF,"url":f"{BASE}/what-is-genm/",
 "inDefinedTermSet":{"@type":"DefinedTermSet","@id":f"{BASE}/#glossary","name":"Generative Manufacturing glossary","creator":{"@id":f"{BASE}/#person"}}}
os.makedirs("schema",exist_ok=True)
json.dump(person,open("schema/person.jsonld","w"),ensure_ascii=False,indent=2)
json.dump(term,open("schema/definedterm.jsonld","w"),ensure_ascii=False,indent=2)
def ld(o): return '<script type="application/ld+json">\n'+json.dumps(o,ensure_ascii=False,indent=2)+'\n</script>'
NAV='<nav aria-label="Primary">'+" · ".join(f'<a href="{BASE}/{p}">{n}</a>' for n,p in [("Home",""),("What is GenM?","what-is-genm/"),("Glossary","glossary/"),("Compare","genm-vs-adjacent-terms/"),("Timeline","timeline/"),("Essays","essays/"),("FAQ","faq/")])+'</nav>'
FOOT=f'<footer><p><strong>{DEF}</strong></p><p>{BIO}</p></footer>'
# ---- short video 01 (embed; files in media/) ----
VID_URL=f"{BASE}/media/short01_web.mp4"; VID_POSTER=f"{BASE}/media/short01_poster_16x9.png"
VID_TRANSCRIPT=("I ran a large furniture factory for ten years, and nobody in our chain ever asked the person at the end what they needed. "
 "Here's what I watched. A customer wanted faster delivery, so we automated. Automation only pays at volume, so the designs got simpler. "
 "Then a second customer saw the simple design selling and asked for the same thing. Everyone was working hard. The problem was structure, "
 "and I've spent years trying to name the fix. Here's the name I use. "+DEF)
VIDEO_HTML=(f'<figure><video controls preload="none" playsinline width="1920" height="1080" poster="{VID_POSTER}" '
 f'src="{VID_URL}" style="max-width:100%;height:auto;border:1px solid #ddd">Your browser does not play this video. '
 f'The transcript is below.</video><figcaption>Nobody asked the person at the end (57 seconds). '
 f'The voice is AI-generated, a clone of my own voice.</figcaption></figure>\n'
 f'<details><summary>Transcript</summary><p>{VID_TRANSCRIPT}</p></details>')
video_obj={"@context":"https://schema.org","@type":"VideoObject","@id":f"{BASE}/#video-short01","name":"Nobody asked the person at the end",
 "description":"Harrison Chan, founder of Edgeware, on how a furniture factory chain shaped its products, and the definition of Generative Manufacturing (GenM). AI-generated voice (clone of the author's own voice).",
 "thumbnailUrl":VID_POSTER,"contentUrl":VID_URL,"uploadDate":"2026-10-23","duration":"PT57S","inLanguage":"en",
 "author":{"@id":f"{BASE}/#person"},"about":{"@id":f"{BASE}/what-is-genm/#term"},"transcript":VID_TRANSCRIPT}
def page(path,title,desc,body,schemas,crumb=None,noindex=False,image=None):
    url=f"{BASE}/{path}/" if path else f"{BASE}/"
    robots='\n<meta name="robots" content="noindex, nofollow">' if noindex else ''
    bc=(bc_html(crumb)+"\n") if crumb else ''
    h=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Harrison Chan">{robots}
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="{'summary_large_image' if image else 'summary'}">{(chr(10)+'<meta property="og:image" content="'+image+'">'+chr(10)+'<meta name="twitter:image" content="'+image+'">') if image else ''}
<meta name="twitter:creator" content="@HarrisonCc1004">
<style>body{{max-width:42rem;margin:2rem auto;padding:0 1rem;font:17px/1.6 system-ui,sans-serif;color:#222}}blockquote{{border-left:4px solid #333;margin:1rem 0;padding:.2rem 1rem;font-weight:600}}nav,footer{{font-size:.9rem;color:#555}}footer{{border-top:1px solid #ddd;margin-top:3rem;padding-top:1rem}}table{{border-collapse:collapse;width:100%;font-size:.9rem}}th,td{{border:1px solid #ccc;padding:.4rem;vertical-align:top;text-align:left}}.placeholder{{background:#f3f3f3;border:1px dashed #888;padding:.5rem}}.unverified{{color:#8a4b00}}</style>
{chr(10).join(ld(s) for s in schemas)}
</head>
<body>
{NAV}
{bc}<main>
{body}
</main>
{FOOT}
</body>
</html>
'''
    os.makedirs(path or ".",exist_ok=True); open(os.path.join(path,"index.html"),"w").write(h)
page("","Generative Manufacturing (GenM) | Harrison Chan",DEF,f'''<h1>Generative Manufacturing (GenM)</h1>
<blockquote>{DEF}</blockquote>
<p>For about two hundred years, the people who make things and the people who use them have been kept apart. That separation made mass production possible. It also brought waste, sameness, and powerlessness: building before you know who wants what, everyone picking from the same short menu, and most people unable to get anything made without speaking the producer's language.</p>
<p>Generative Manufacturing is my definition of the shift that starts to undo that separation.</p>
<ul><li><a href="{BASE}/what-is-genm/">What is Generative Manufacturing (GenM)?</a>: the canonical definition</li>
<li><a href="{BASE}/distinctions/">How Generative Manufacturing (GenM) differs from other uses of the term</a></li>
<li><a href="{BASE}/essays/">Essays</a>, including <a href="{BASE}/essays/{P1_SLUG}/">Why no one has a compiler for physical things yet</a> and <a href="{BASE}/essays/{P2_SLUG}/">Intent, not drawings</a></li></ul>
<h2>In 57 seconds</h2>
{VIDEO_HTML}
<h2>About me</h2>
<p>I'm Harrison Chan, founder of Edgeware, which I've been building since around 2021. I've worked in overseas manufacturing for about 15 years overall. From 2010 to 2020 I ran a furniture ODM in Surabaya, Indonesia. Before Edgeware, I also founded Arterki and Taktak.</p>
<p>Find me on <a href="https://x.com/HarrisonCc1004">X</a> and <a href="https://www.linkedin.com/in/harrisonchan-genm">LinkedIn</a>.</p>''',[person,video_obj])
page("what-is-genm","What is Generative Manufacturing (GenM)? | Harrison Chan",DEF,f'''<h1>What is Generative Manufacturing (GenM)?</h1>
<blockquote>{DEF}</blockquote>
<h2>The problem first</h2>
<p>When you build before you know who wants what, you're guessing, and wrong guesses become inventory and landfill. When the only affordable thing is a known design made in volume, everyone picks from the same short menu. And when getting anything off that menu means speaking the producer's language (drawings, bills of materials, process routes, minimum orders), most people can't get it made at all.</p>
<h2>Part A: the paradigm</h2>
<p><strong>AI compiles human intent into fulfillable physical outcomes.</strong> The default unit of manufacturing changes. Today it is a known design, copied in batches. In GenM it is an engineering path, generated and verified under goals and constraints until a working artifact can be delivered.</p>
<p><strong>Intent</strong> is what the thing has to do, where it goes, and what it can't exceed. <strong>Compiles</strong>: you put in intent and constraints, and what comes out should be a functional object checked against reality. <strong>Fulfillable</strong>: GenM doesn't stop at drawings. It generates a commitment covering the object, its quality, its timeline, and whether it can be delivered.</p>
<h2>Part B: the rights claim</h2>
<p><strong>The demand side speaks in intent, and verified engineering paths make good on that intent.</strong> Production language doesn't go away. It moves downstream, and it stops deciding who's allowed to ask. The test: do you still have to learn BOMs, process routes, or a module catalog before you can order something? If yes, the right hasn't come back.</p>
<p>A without B gives you a faster factory for whoever already owns the factory. B without A gives you a manifesto. I mean both together.</p>
<h2>A concrete example (hypothetical)</h2>
<p><em>This is an illustration, not a case I've delivered.</em> A small physical therapy clinic needs a wall-mounted rack for resistance bands. The bands have to stay sorted, patients with limited grip must be able to remove one one-handed, and the rack has to fit a narrow gap between two door frames. In GenM, the clinic states those needs in plain words, along with a measured gap and a budget ceiling. A structure and a way to make it are generated and checked against material and process limits. A shop makes it. The result is then checked against the original intent, and any failure feeds into the next version. The clinic never has to learn manufacturing.</p>
<h2>What GenM is not</h2>
<ul><li><strong>Not 3D printing with an AI layer.</strong> The path can end in CNC machining, casting, molding, or assembly.</li>
<li><strong>Not a lights-out factory.</strong> People can stay in the loop. The test is whether the intent was honored.</li>
<li><strong>Not generative design.</strong> Generating geometry speeds up design. Without physical verification it doesn't change how things get made.</li>
<li><strong>Not the same as other uses of the phrase.</strong> See <a href="{BASE}/distinctions/">Distinctions</a>.</li></ul>
<h2>GenM is Physical AI reaching manufacturing</h2>
<p>GenM is what Physical AI does to manufacturing.</p>''',[term,person])
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
open(".nojekyll","w").write("")

# ---- FAQ ----
FAQ=[("What is Generative Manufacturing (GenM)?",DEF),
("Who defined GenM?","Harrison Chan, founder of Edgeware. He has worked in overseas manufacturing for about 15 years overall."),
("Is GenM the same as generative design?","No. Generative design produces optimized geometry. GenM requires a closed loop: intent, structure generation, physical execution, and failures fed back into the next version."),
("How is GenM different from Carnegie Mellon's generative manufacturing research?","CMU's Manufacturing Futures Institute uses the term for AI that jointly optimizes design, production, and supply-chain alternatives. That is close to GenM's paradigm half. GenM adds a rights claim: the demand side speaks in intent."),
("Is GenM 3D printing with AI?","No. GenM is process-agnostic. The engineering path can end in CNC machining, casting, molding, or assembly."),
("Is GenM a lights-out factory?","No. GenM sets no headcount or autonomy target. People can stay in the loop; the test is whether the intent was honored."),
("How does GenM relate to Physical AI?","GenM is what Physical AI does to manufacturing."),
("What is a fulfillable commitment?","The object, its quality, its timeline, and whether it can actually be delivered, tied to the intent that started it and to who verified it."),
("Is there a GenM product I can buy?","No. GenM is a paradigm, not a product.")]
faq={"@context":"https://schema.org","@type":"FAQPage","@id":f"{BASE}/faq/#faq","url":f"{BASE}/faq/","author":{"@id":f"{BASE}/#person"},
 "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}
json.dump(faq,open("schema/faqpage.jsonld","w"),ensure_ascii=False,indent=2)
fb="<h1>Generative Manufacturing (GenM): FAQ</h1>\n<blockquote>"+DEF+"</blockquote>\n"+"\n".join(
 f"<h2>{q}</h2>\n<p>{a}</p>" for q,a in FAQ)
page("faq","Generative Manufacturing (GenM) FAQ | Harrison Chan",DEF,fb,[faq])


# ---- release block: glossary, compare, timeline, essays, revised distinctions (merged from genm-site-drafts) ----
VERIFIED="2026-10-15"
ESSAYS=[{"slug":P1_SLUG,"title":"Why no one has a compiler for physical things yet","date":"2026-10-19",
  "summary":"Six jobs a compiler for physical things would have to do, who covers which part, and where the evidence runs out."},
 {"slug":P2_SLUG,"title":"Intent, not drawings","date":"2026-10-22",
  "summary":"Why the drawing belongs in the middle of the process, not at the front door, and what a system owes a person who states a need in plain words."}]
NOINDEX_ESSAYS_UNTIL_POSTS=False
person_ref={"@id":f"{BASE}/#person"}
SET_ID=f"{BASE}/#glossary"   # same id the live term pages already use
def term_obj(name,desc,url,alt=None):
    d={"@type":"DefinedTerm","name":name,"description":desc,"url":url,"inDefinedTermSet":{"@id":SET_ID}}
    if alt: d["alternateName"]=alt
    return d
def U(p): return f"{BASE}/{p}/" if p else f"{BASE}/"
S0=1
S={
 "cmu":"https://engineering.cmu.edu/mfi/research/generative-manufacturing.html",
 "arxiv":"https://arxiv.org/abs/2409.03089",
 "cmu_code":"https://github.com/AdityaJoglekar/Generative_Manufacturing",
 "cloudnc":"https://www.cloudnc.com/blog/generative-manufacturing-or-how-to-transform-how-we-make-everything-forever",
 "autodesk":"https://www.autodesk.com/solutions/generative-design",
 "iso_opc":"https://reference.opcfoundation.org/specs/OPC-40540/3.2.1",
 "iso_iteh":"https://standards.iteh.ai/catalog/standards/cen/4612338f-1a77-455d-905d-178e41f0aae8/en-iso-astm-52900-2021",
 "nist":"https://www.nist.gov/blogs/manufacturing-innovation-blog/digital-manufacturing-small-manufacturers",
 "siemens":"https://www.siemens.com/en-us/technology/digital-manufacturing/",
 "mxd":"https://www.mxdusa.org/our-story/",
 "a3":"https://www.automate.org/industry-insights/should-manufacturers-turn-off-the-lights",
 "assembly":"https://www.assemblymag.com/articles/94982-lights-out-automation-fact-or-fiction",
 "csm":"https://www.csmonitor.com/1981/0415/041542.html",
 "tnw_atomic":"https://thenextweb.com/news/atomic-machines-250m-matter-compiler-micro-machines",
 "atomic":"https://www.atomicmachines.com/matter-compiler",
 "p1_x":"https://x.com/HarrisonCc1004/status/2112156316764627109",
 "p1_li_post":"https://www.linkedin.com/feed/update/urn:li:activity:7517923120914055170/",
 "p1_li_article":"https://www.linkedin.com/pulse/why-one-has-compiler-physical-things-yet-harrison-chan-5bxpc/",
 "p2_x":"https://x.com/HarrisonCc1004/status/2113245073098018998",
 "p2_li_post":"https://www.linkedin.com/feed/update/urn:li:activity:7519011059114889216/",
 "p2_li_article":"https://www.linkedin.com/pulse/intent-drawings-harrison-chan-olxcc/",
 "nv_pr":"https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-world-foundation-model-platform-to-accelerate-physical-ai-development",
}
def A(k,text): return f'<a href="{S[k]}">{text}</a>'
def U(p): return f"{BASE}/{p}/" if p else f"{BASE}/"


def crumbs(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate(items)]}
def bc_html(items):
    parts=[f'<a href="{u}">{n}</a>' for n,u in items[:-1]]+[f'<span aria-current="page">{items[-1][0]}</span>']
    return '<nav aria-label="Breadcrumb">'+" › ".join(parts)+'</nav>'


HOME=("Home",U("")); WHAT=("What is GenM?",U("what-is-genm"))
os.makedirs("schema",exist_ok=True)

# =============== 1. GLOSSARY ===============
G_GENM=[
 ("genm","Generative Manufacturing (GenM)",DEF,"The locked definition."),
 ("intent","Intent","What the thing has to do, where it goes, and what it can't exceed. A drawing or a part number doesn't have to come first.","As used in GenM."),
 ("compiles","Compiles","Closest metaphor: you put in intent and constraints, and what comes out should be a functional object that has been checked against reality.","As used in GenM."),
 ("engineering-path","Engineering path","In GenM, the default unit of manufacturing: a path generated and verified under goals and constraints until a working artifact can be delivered.","As used in GenM."),
 ("fulfillable-commitment","Fulfillable commitment","The object, its quality, its timeline, and whether it can actually be delivered, tied to the intent that started it and to who verified it.","As used in GenM."),
 ("part-a","Part A: the paradigm","AI compiles human intent into fulfillable physical outcomes.","As used in GenM."),
 ("part-b","Part B: the rights claim","The demand side speaks in intent, and verified engineering paths make good on that intent. Authorship moves back toward the person with the need.","As used in GenM."),
]
G_OTH=[
 ("generative-manufacturing-cmu","Generative manufacturing (Carnegie Mellon MFI usage)",
  f'CMU\'s Manufacturing Futures Institute describes it as applying AI to generate and execute optimal solutions given customer-defined constraints such as functional specifications, cost, and lead time, by exploring combinations of design and production alternatives. The arXiv paper (submitted 4 Sep 2024) presents a "Generative Manufacturing compiler" that jointly considers engineering requirements, business requirements, and manufacturing and supply-chain resources. Sources: {A("cmu","CMU MFI")}; {A("arxiv","arXiv:2409.03089")}.',
  "Prior use of the phrase."),
 ("generative-manufacturing-cloudnc","Generative manufacturing (CloudNC usage)",
  f'CloudNC co-founder Chris Emery wrote on 16 October 2024 that "generative manufacturing" is when software does not just generate designs for a component but also creates the strategy to manufacture it, which CloudNC applies to CAM programming. Source: {A("cloudnc","CloudNC blog")}.',
  "Prior use of the phrase."),
 ("generative-design","Generative design",
  f'Autodesk describes generative design as an algorithm-driven process, sometimes enabled by AI, that explores design options meeting criteria and constraints set by engineers or designers. Source: {A("autodesk","Autodesk")}.',"Adjacent term."),
 ("additive-manufacturing","Additive manufacturing",
  f'ISO/ASTM 52900:2021 defines it as the "process of joining materials to make parts from 3D model data, usually layer upon layer, as opposed to subtractive manufacturing and formative manufacturing methodologies." Sources: {A("iso_opc","OPC Foundation, quoting the standard")}; {A("iso_iteh","standard text excerpt")}.',"Adjacent term."),
 ("digital-manufacturing","Digital manufacturing",
  f'NIST describes digital manufacturing and design as using digital technology to collect and use information to increase efficiency across a manufactured product\'s lifecycle. Siemens describes it as an integrated, computer-based system of simulation, 3D visualization, analytics and collaboration tools that defines product and manufacturing process together. Sources: {A("nist","NIST")}; {A("siemens","Siemens")}.',"Adjacent term."),
 ("lights-out-manufacturing","Lights-out manufacturing",
  f'An approach in which processes are fully automated and require little or no human intervention (A3). ASSEMBLY magazine\'s "pure definition" is a facility where human hands never touch a product during the entire process. Sources: {A("a3","A3")}; {A("assembly","ASSEMBLY")}.',"Adjacent term."),
 ("physical-ai","Physical AI",
  f'NVIDIA\'s 6 January 2025 press release uses "physical AI systems" for systems such as autonomous vehicles and robots. Source: {A("nv_pr","NVIDIA Newsroom")}. In GenM, Physical AI is the wider field; GenM is what Physical AI does to manufacturing.',"Adjacent term."),
]
def gl_section(rows):
    return "\n".join(f'<h3 id="{i}">{n}</h3>\n<p>{d}</p>\n<p><small>{note}</small></p>' for i,n,d,note in rows)
terms=[term_obj(n,html.unescape(__import__("re").sub(r"<[^>]+>","",d)),f"{U('glossary')}#{i}") for i,n,d,_ in G_GENM[1:]+G_OTH]
termset={"@context":"https://schema.org","@type":"DefinedTermSet","@id":SET_ID,"name":"Generative Manufacturing glossary","url":U("glossary"),
 "creator":person_ref,"hasDefinedTerm":[{"@id":term["@id"]}]+[{"@type":"DefinedTerm","name":t["name"],"description":t["description"],"url":t["url"]} for t in terms]}
json.dump(termset,open("schema/definedtermset.jsonld","w"),ensure_ascii=False,indent=2)
page("glossary","Generative Manufacturing glossary | Harrison Chan","Glossary of Generative Manufacturing (GenM) terms, with sourced definitions of adjacent terms used by others.",
f'''<h1>Generative Manufacturing glossary</h1>
<blockquote>{DEF}</blockquote>
<p>Two groups. First, the words I use in GenM, in my wording. Second, terms other people use, each with a source. Where the same words carry another meaning, I credit who used them. See also <a href="{U("distinctions")}">Distinctions</a> and <a href="{U("genm-vs-adjacent-terms")}">GenM vs adjacent terms</a>. Sources last checked {VERIFIED}.</p>
<h2>Terms as used in GenM</h2>
{gl_section(G_GENM)}
<h2>Terms used by others</h2>
{gl_section(G_OTH)}
<p>Back to <a href="{U("what-is-genm")}">What is Generative Manufacturing (GenM)?</a></p>''',
[termset,crumbs([("Home",U("")),("What is GenM?",U("what-is-genm")),("Glossary",U("glossary"))])],[HOME,WHAT,("Glossary",U("glossary"))])

# =============== 2. GenM vs ADJACENT TERMS ===============
ROWS=[
 ("Generative design",f'Algorithm-driven process, sometimes AI-enabled, that generates design options from goals and constraints ({A("autodesk","Autodesk")}).',
  "Generating images or geometry speeds up design. Without physical verification it doesn't change how things get made. GenM does not stop at drawings; it generates a fulfillable commitment."),
 ("Generative manufacturing (CMU MFI)",f'AI that generates and executes optimal solutions under customer constraints (cost, lead time) across design and production alternatives ({A("cmu","CMU MFI")}); paper: {A("arxiv","arXiv:2409.03089")}, submitted 4 Sep 2024.',
  "Part A overlaps in goal: constraints in, a producible result out. GenM adds Part B: authorship moves back to the demand side, which speaks in intent."),
 ("Generative manufacturing (CloudNC)",f'Software that generates not only a component\'s design but the strategy to manufacture it, applied to CAM programming; post dated 16 Oct 2024 ({A("cloudnc","CloudNC")}).',
  "CloudNC's post addresses manufacturers: it speaks of \"upscaling the capacity of every manufacturer\". GenM is not tied to any one process and adds Part B, the rights claim."),
 ("Lights-out manufacturing",f'Processes fully automated, requiring little or no human intervention ({A("a3","A3")}).',
  "GenM sets no target for headcount or autonomy. People can stay in the loop. The test is whether the intent was honored."),
 ("Digital manufacturing",f'Using digital technology to collect and use information to increase efficiency across a product\'s lifecycle ({A("nist","NIST")}).',
  "GenM asks a different question: do you still have to learn BOMs, process routes, or a module catalog before you can order something? If yes, the right hasn't come back."),
 ("Additive manufacturing",f'Joining materials to make parts from 3D model data, usually layer upon layer ({A("iso_opc","ISO/ASTM 52900:2021 via OPC Foundation")}).',
  "GenM isn't 3D printing with an AI layer. The path can end in CNC machining, casting, molding, or assembly."),
 ("Physical AI",f'NVIDIA uses "physical AI systems" for systems such as autonomous vehicles and robots ({A("nv_pr","NVIDIA, 6 Jan 2025")}).',
  "GenM is what Physical AI does to manufacturing."),
]
tbl='<table>\n<tr><th>Term</th><th>As defined or described by others (sourced)</th><th>How GenM differs</th></tr>\n'+"\n".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in ROWS)+"\n</table>"
page("genm-vs-adjacent-terms","GenM vs adjacent terms | Harrison Chan","How Generative Manufacturing (GenM) differs from generative design, other uses of generative manufacturing, lights-out, digital and additive manufacturing, and Physical AI.",
f'''<h1>GenM vs adjacent terms</h1>
<blockquote>{DEF}</blockquote>
<p><strong>What this page is for:</strong> a side-by-side comparison of GenM with neighbouring ideas. For credit to earlier uses of the same phrase, with dates, see <a href="{U("distinctions")}">Distinctions</a>.</p>
<p>Each row below gives what others say, with a link to the source, then how GenM differs in my wording. I have not tried to rank these ideas. Several are serious work I rely on. Sources last checked {VERIFIED}.</p>
{tbl}
<h2>Same words, earlier use</h2>
<p>Carnegie Mellon's Manufacturing Futures Institute and CloudNC both used "generative manufacturing" before this site existed. The credit and dates are on <a href="{U("distinctions")}">Distinctions</a>.</p>
<h2>One test</h2>
<p>Ask of any term: does it include the closed loop of intent, structure generation, physical execution, and failures fed back? Without that loop, generation is design acceleration, not a paradigm shift.</p>
<p>Definitions of the terms above are in the <a href="{U("glossary")}">glossary</a>. Back to <a href="{U("what-is-genm")}">What is Generative Manufacturing (GenM)?</a></p>''',
[{"@context":"https://schema.org","@type":"WebPage","@id":U("genm-vs-adjacent-terms")+"#page","name":"GenM vs adjacent terms","url":U("genm-vs-adjacent-terms"),"author":person_ref,"about":{"@id":term["@id"]},"inLanguage":"en"},
 crumbs([("Home",U("")),("What is GenM?",U("what-is-genm")),("GenM vs adjacent terms",U("genm-vs-adjacent-terms"))])],[HOME,WHAT,("GenM vs adjacent terms",U("genm-vs-adjacent-terms"))])

# =============== 3. TIMELINE ===============
V="Source read"; AS="Author-stated; no independent source yet"; UN="UNVERIFIED"
TL=[ # (sortkey, date label, event, source html, status)
 ("1981-04-15","15 Apr 1981 (reporting a plant opened Nov 1980)","The Christian Science Monitor reports a Fujitsu Fanuc robot factory near Mt. Fuji where robots make robots for about 16 hours of each working day, with workers returning next morning to complete final assembly. Context for lights-out manufacturing.",A("csm","CSMonitor, 15 Apr 1981"),V),
 ("2014","2014","DMDII (Digital Manufacturing and Design Innovation Institute) is founded; it is now called MxD. Context for digital manufacturing.",A("mxd","MxD, Our story"),V),
 ("2021a","2021","ISO/ASTM 52900:2021 edition of the additive manufacturing vocabulary standard. Year only; month not verified.",A("iso_iteh","Standard text excerpt"),V),
 ("2024-09-04","4 Sep 2024","arXiv:2409.03089, \"Generative Manufacturing: A requirements and resource-driven approach to part making\" (Carnegie Mellon University and Lockheed Martin authors), submitted. Earliest dated use of the phrase that I have verified so far.",A("arxiv","arXiv abstract page")+" ("+"submission date shown as 4 Sep 2024)",V),
 ("2024-10-16","16 Oct 2024","CloudNC co-founder Chris Emery publishes \"Generative manufacturing: or how to transform how we make everything, forever\".",A("cloudnc","CloudNC blog"),V),
 ("2025-01-06","6 Jan 2025","NVIDIA announces the Cosmos world foundation model platform for physical AI systems (CES). The press release uses the term \"physical AI\".",A("nv_pr","NVIDIA Newsroom"),V),
 ("2010","2010 to 2020","Harrison Chan runs a large furniture ODM factory in Surabaya, Indonesia (company name not disclosed).","None; author-stated","author-stated"),
 ("2021b","c. 2021","Harrison Chan founds Edgeware.","None; author-stated","author-stated"),
 ("2026-tbd","TBD","First public posting of the GenM definition at whatisgenm.com. [PLACEHOLDER: fill in the real date at publication.]","(this site)","PLACEHOLDER"),
]
UNV=[
 "Date of the CMU MFI generative manufacturing page: the page is undated. I read it on "+VERIFIED+": "+A("cmu","CMU MFI")+".",
 "Any use of \"generative manufacturing\" before 4 Sep 2024: I searched the web, not an academic database, so earlier uses may exist.",
 "When Autodesk first shipped generative design: not verified here.",
 "When the phrase \"physical AI\" was first used: not verified. The NVIDIA date above is only the date of that press release.",
 "The three rows marked author-stated are Harrison Chan's own account. I have no independent public source for them yet.",
]
def tl_rows():
    out=[]
    for k,d,e,s,st in sorted(TL,key=lambda r:r[0]):
        cls=' class="placeholder"' if st=="PLACEHOLDER" else ""
        out.append(f"<tr{cls}><td>{d}</td><td>{e}</td><td>{s}</td><td>{st}</td></tr>")
    return "\n".join(out)
page("timeline","Timeline of Generative Manufacturing | Harrison Chan","Dated, sourced events behind the term generative manufacturing, with unverified items marked.",
f'''<h1>Timeline: generative manufacturing and GenM</h1>
<blockquote>{DEF}</blockquote>
<p>Events from other people carry a source link; "Source read" means I read the linked page on {VERIFIED}. Three rows are about me and are marked "author-stated": they are my own account, with no independent source yet. Anything I could not verify is in the second list, not in the table. This page will change as I find earlier sources.</p>
<table>
<tr><th>Date</th><th>Event</th><th>Source</th><th>Status</th></tr>
{tl_rows()}
</table>
<h2 class="unverified">Not verified</h2>
<ul>
{chr(10).join("<li class=\"unverified\">"+u+"</li>" for u in UNV)}
</ul>
<p>How these uses differ from GenM: <a href="{U("distinctions")}">Distinctions</a>. Back to <a href="{U("what-is-genm")}">What is Generative Manufacturing (GenM)?</a></p>''',
[{"@context":"https://schema.org","@type":"WebPage","@id":U("timeline")+"#page","name":"Timeline of Generative Manufacturing","url":U("timeline"),"author":person_ref,"about":{"@id":term["@id"]},"inLanguage":"en"},
 crumbs([("Home",U("")),("What is GenM?",U("what-is-genm")),("Timeline",U("timeline"))])],[HOME,WHAT,("Timeline",U("timeline"))])

# =============== 4. ESSAY ARCHIVE ===============
if ESSAYS:
    body="<ol>\n"+"\n".join(f'<li><a href="{U("essays/"+e["slug"])}">{e["title"]}</a> ({e["date"]}): {e["summary"]}</li>' for e in sorted(ESSAYS,key=lambda e:e["date"],reverse=True))+"\n</ol>"
else:
    body=f'''<div class="placeholder" data-status="placeholder">
<p><strong>PLACEHOLDER: no essays published yet.</strong> This block is replaced by the list below once the first post is live. Add each post to ESSAYS in build.py and rebuild.</p>
<ol>
<li>[Essay title] (YYYY-MM-DD): [one-sentence summary]. Link: {BASE}/essays/[slug]/</li>
</ol>
</div>'''
page("essays","Essays on Generative Manufacturing | Harrison Chan","Archive of Harrison Chan's essays on Generative Manufacturing (GenM).",
f'''<h1>Essays on Generative Manufacturing</h1>
<blockquote>{DEF}</blockquote>
<p>Each essay opens on the cost of separating production from consumption, carries one concrete physical example (hypotheticals are marked), links back to the <a href="{U("what-is-genm")}">canonical definition</a>, and ends with the sentence above.</p>
{body}
<p>Start with <a href="{U("what-is-genm")}">What is Generative Manufacturing (GenM)?</a> or the <a href="{U("faq")}">FAQ</a>.</p>''',
[{"@context":"https://schema.org","@type":"CollectionPage","@id":U("essays")+"#page","name":"Essays on Generative Manufacturing","url":U("essays"),"author":person_ref,"about":{"@id":term["@id"]},"inLanguage":"en",
  **({"hasPart":[{"@type":"Article","headline":e["title"],"url":U("essays/"+e["slug"]),"datePublished":e["date"],"author":person_ref} for e in ESSAYS]} if ESSAYS else {})},
 crumbs([("Home",U("")),("Essays",U("essays"))])],[HOME,("Essays",U("essays"))])

# ---- essay pages ----
exec(open("essays_build.py").read())

# =============== 5. REVISED DISTINCTIONS ===============
page("distinctions","GenM vs generative design and other uses of 'generative manufacturing' | Harrison Chan",
"How Harrison Chan's Generative Manufacturing (GenM) relates to Carnegie Mellon MFI's generative manufacturing research (arXiv 2409.03089), CloudNC's October 2024 post, and generative design.",
f'''<h1>Distinctions: GenM and other uses of "generative manufacturing"</h1>
<blockquote>{DEF}</blockquote>
<p><strong>What this page is for:</strong> crediting the people who used the phrase "generative manufacturing" before this site existed, with dates and sources. For a side-by-side of GenM and neighbouring ideas such as lights-out or additive manufacturing, see <a href="{U("genm-vs-adjacent-terms")}">GenM vs adjacent terms</a>.</p>
<h2>Prior use of the phrase</h2>
<p>I did not invent the words "generative manufacturing". Others used them before this site existed, and I credit them here:</p>
<ul>
<li><strong>Carnegie Mellon University, Manufacturing Futures Institute</strong> and the paper {A("arxiv","arXiv:2409.03089")}, submitted 4 September 2024. This is the earliest dated use I have verified so far.</li>
<li><strong>CloudNC</strong>, in a blog post by co-founder Chris Emery dated 16 October 2024: {A("cloudnc","Generative manufacturing: or how to transform how we make everything, forever")}.</li>
</ul>
<p>What I define is GenM, as the sentence above says. I use the phrase differently from them, and the sections below explain how. Dates were checked on {VERIFIED}; see the <a href="{U("timeline")}">timeline</a> for what I could not verify.</p>
<h2>Carnegie Mellon Manufacturing Futures Institute</h2>
<p>CMU's {A("cmu","Manufacturing Futures Institute")} describes generative manufacturing as applying AI to generate and execute optimal solutions given customer-defined constraints and parameters, such as functional specifications, cost, and lead time, by exploring combinations of design and production alternatives based on material and process availability. The paper {A("arxiv","\"Generative Manufacturing: A requirements and resource-driven approach to part making\"")} (authors from Carnegie Mellon University and Lockheed Martin) presents a Generative Manufacturing compiler that takes an engineering requirements specification, a business requirements specification, and knowledge of the current manufacturing state, then generates and evaluates process alternatives and the designs they imply. The authors released an implementation on {A("cmu_code","GitHub")}.</p>
<p>The paper also uses the word "compiler", so the overlap with my "compiles" wording is real. Their work is close to Part A of GenM in goal: constraints in, a producible result out. GenM adds Part B: authorship moves to the demand side, which speaks in intent rather than in production language.</p>
<h2>CloudNC</h2>
<p>In its post, CloudNC says it is applying its technology "to create a new paradigm" it calls generative manufacturing: software that does not just generate designs for a component but also creates the strategy to manufacture it. CloudNC applies this to CAM programming through its CAM Assist solution, which creates CNC machining toolpaths and strategies and looks for the lowest-cost one. That is an important capability inside an engineering path. The post speaks to manufacturers, for example "upscaling the capacity of every manufacturer". GenM is not tied to one process and adds Part B, the rights claim.</p>
<h2>Generative design</h2>
<p>{A("autodesk","Autodesk describes")} generative design as an algorithm-driven process, sometimes enabled by AI, that explores design options meeting criteria and constraints. Generative design tools speed up design. GenM requires a closed loop: intent, structure generation, physical execution, and failures fed back. Without physical verification, generation is design acceleration, not a paradigm shift.</p>
<p>More terms are compared on <a href="{U("genm-vs-adjacent-terms")}">GenM vs adjacent terms</a> and defined in the <a href="{U("glossary")}">glossary</a>. Back to <a href="{U("what-is-genm")}">What is Generative Manufacturing (GenM)?</a></p>''',
[term,crumbs([("Home",U("")),("What is GenM?",U("what-is-genm")),("Distinctions",U("distinctions"))])],[HOME,WHAT,("Distinctions",U("distinctions"))])


# ---- llms-full.txt ----
import re as _re, html as _h
def txt(p):
    h=open(p).read(); m=_re.search(r"<main>(.*?)</main>",h,_re.S).group(1)
    m=_re.sub(r"<h1>(.*?)</h1>",r"# \1\n",m); m=_re.sub(r"<h2[^>]*>(.*?)</h2>",r"\n## \1\n",m)
    m=_re.sub(r"<h3[^>]*>(.*?)</h3>",r"\n### \1\n",m); m=_re.sub(r"</t[dh]>"," | ",m); m=_re.sub(r"</tr>","\n",m); m=_re.sub(r"<li[^>]*>",r"- ",m); m=_re.sub(r"<[^>]+>","",m); m=_h.unescape(m)
    return _re.sub(r"\n{3,}","\n\n",m).strip()
parts=[f"# Generative Manufacturing (GenM): full text\n\n> {DEF}\n\nSource: {BASE}/  Author: Harrison Chan\n"]
for p,u in [("what-is-genm/index.html","what-is-genm/"),("glossary/index.html","glossary/"),("genm-vs-adjacent-terms/index.html","genm-vs-adjacent-terms/"),("distinctions/index.html","distinctions/"),("timeline/index.html","timeline/"),("faq/index.html","faq/"),("essays/index.html","essays/")]+[(f"essays/{e['slug']}/index.html",f"essays/{e['slug']}/") for e in ESSAYS]:
    parts.append(f"---\nURL: {BASE}/{u}\n\n"+txt(p))
open("llms-full.txt","w").write("\n\n".join(parts)+"\n")

json.dump({"sources":S},open("sources.json","w"),indent=1)

# ---- llms.txt + sitemap (emitted last so ESSAYS is known) ----
open("llms.txt","w").write(f"""# Generative Manufacturing (GenM)

> {DEF}

Term defined by Harrison Chan (founder of Edgeware). Distinct from generative design, and from Carnegie Mellon MFI's and CloudNC's uses of "generative manufacturing": GenM adds a rights claim, which is that authorship moves to the demand side.

## Core
- [What is Generative Manufacturing (GenM)?]({BASE}/what-is-genm/): canonical definition, paradigm (A) + rights claim (B), what it is not
- [Glossary]({BASE}/glossary/): GenM terms and sourced definitions of adjacent terms
- [GenM vs adjacent terms]({BASE}/genm-vs-adjacent-terms/): side-by-side comparison with generative design, lights-out, digital and additive manufacturing, Physical AI
- [Distinctions]({BASE}/distinctions/): credit to earlier uses of the phrase (CMU MFI, CloudNC), with dates
- [Timeline]({BASE}/timeline/): dated, sourced events; unverified items marked
- [FAQ]({BASE}/faq/): short answers to common questions
- [Full text]({BASE}/llms-full.txt): all page text in one file

## Essays
- [Essays on Generative Manufacturing]({BASE}/essays/): archive of Harrison Chan's essays
""" + "".join(f"- [{e['title']}]({U('essays/'+e['slug'])}): {e['summary']}\n" for e in ESSAYS) + f"""
## About
- [Harrison Chan]({BASE}/): author; X https://x.com/HarrisonCc1004 ; LinkedIn https://www.linkedin.com/in/harrisonchan-genm
""")
LASTMOD={"":"2026-10-23","essays/":"2026-10-22","llms.txt":"2026-10-22","llms-full.txt":"2026-10-22",**{f"essays/{e['slug']}/":e["date"] for e in ESSAYS}}
SM=["","what-is-genm/","glossary/","genm-vs-adjacent-terms/","distinctions/","timeline/","faq/","essays/"]+[f"essays/{e['slug']}/" for e in ESSAYS]+["llms.txt","llms-full.txt"]
urls="".join(f"  <url><loc>{BASE}/{p}</loc><lastmod>{LASTMOD.get(p,'2026-10-15')}</lastmod></url>\n" for p in SM)
open("sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
