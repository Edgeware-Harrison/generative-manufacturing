import json, os
BASE="https://whatisgenm.com"
DEF="Generative Manufacturing (GenM) is the manufacturing paradigm in which AI compiles human intent into fulfillable physical outcomes, so the demand side speaks in intent and verified engineering paths make good on it."
BIO="Harrison Chan — defining Generative Manufacturing (GenM); head of Miracle Plus Physical AI Lab; founder of Edgeware."
person={"@context":"https://schema.org","@type":"Person","@id":f"{BASE}/#person","name":"Harrison Chan","description":BIO,
 "jobTitle":"Head of Miracle Plus Physical AI Lab","worksFor":{"@type":"Organization","name":"Miracle Plus Physical AI Lab"},
 "knowsAbout":["Generative Manufacturing","Physical AI","Overseas manufacturing"],
 "url":f"{BASE}/","sameAs":["https://x.com/HarrisonCc1004","https://www.linkedin.com/in/harrisonchan-genm","https://github.com/Edgeware-Harrison"]}
term={"@context":"https://schema.org","@type":"DefinedTerm","@id":f"{BASE}/what-is-genm/#term","name":"Generative Manufacturing",
 "alternateName":["GenM","生成式制造"],"description":DEF,"url":f"{BASE}/what-is-genm/",
 "inDefinedTermSet":{"@type":"DefinedTermSet","@id":f"{BASE}/#glossary","name":"Generative Manufacturing glossary","creator":{"@id":f"{BASE}/#person"}}}
os.makedirs("schema",exist_ok=True)
json.dump(person,open("schema/person.jsonld","w"),ensure_ascii=False,indent=2)
json.dump(term,open("schema/definedterm.jsonld","w"),ensure_ascii=False,indent=2)
def ld(o): return '<script type="application/ld+json">\n'+json.dumps(o,ensure_ascii=False,indent=2)+'\n</script>'
NAV=f'<nav><a href="{BASE}/">Home</a> · <a href="{BASE}/what-is-genm/">What is GenM?</a> · <a href="{BASE}/distinctions/">Distinctions</a> · <a href="{BASE}/faq/">FAQ</a></nav>'
FOOT=f'<footer><p><strong>{DEF}</strong></p><p>{BIO}</p></footer>'
def page(path,title,desc,body,schemas):
    url=f"{BASE}/{path}/" if path else f"{BASE}/"
    h=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Harrison Chan">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<meta name="twitter:creator" content="@HarrisonCc1004">
<style>body{{max-width:42rem;margin:2rem auto;padding:0 1rem;font:17px/1.6 system-ui,sans-serif;color:#222}}blockquote{{border-left:4px solid #333;margin:1rem 0;padding:.2rem 1rem;font-weight:600}}nav,footer{{font-size:.9rem;color:#555}}footer{{border-top:1px solid #ddd;margin-top:3rem;padding-top:1rem}}</style>
{chr(10).join(ld(s) for s in schemas)}
</head>
<body>
{NAV}
<main>
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
<p>Generative Manufacturing is my name for the shift that starts to undo that separation.</p>
<ul><li><a href="{BASE}/what-is-genm/">What is Generative Manufacturing (GenM)?</a>: the canonical definition</li>
<li><a href="{BASE}/distinctions/">How GenM differs from other uses of the term</a></li></ul>
<h2>About me</h2>
<p>I'm Harrison Chan. I've been head of Miracle Plus Physical AI Lab since September 2026. I've worked in overseas manufacturing for about 15 years overall. From 2010 to 2020 I ran a furniture ODM in Surabaya, Indonesia. I founded Arterki and Taktak, and I've been building Edgeware since around 2021.</p>
<p>Find me on <a href="https://x.com/HarrisonCc1004">X</a> and <a href="https://www.linkedin.com/in/harrisonchan-genm">LinkedIn</a>.</p>''',[person])
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
page("distinctions","GenM vs generative design and other uses of 'generative manufacturing'","How Harrison Chan's Generative Manufacturing (GenM) relates to Carnegie Mellon MFI's generative manufacturing research, CloudNC's use of the term, and generative design.",f'''<h1>Distinctions: GenM and other uses of "generative manufacturing"</h1>
<blockquote>{DEF}</blockquote>
<p>Others have used the words "generative manufacturing" before me, and their work is serious. Here is how my definition relates to theirs.</p>
<h2>Carnegie Mellon Manufacturing Futures Institute</h2>
<p>CMU's <a href="https://engineering.cmu.edu/mfi/research/generative-manufacturing.html">Manufacturing Futures Institute</a> describes generative manufacturing as applying AI to generate and execute optimal solutions given customer-defined constraints such as functional specifications, cost, and lead time, by exploring combinations of design and production alternatives based on material and process availability. The paper <a href="https://arxiv.org/abs/2409.03089">"Generative Manufacturing: A requirements and resource-driven approach to part making"</a> (arXiv:2409.03089) presents a compiler that jointly considers engineering requirements, business requirements, and manufacturing and supply-chain resources.</p>
<p>That work is close to Part A of GenM, and an optimizer like it could power that half. GenM adds Part B: authorship moves to the demand side, which speaks in intent rather than in production language.</p>
<h2>CloudNC</h2>
<p>CloudNC uses "generative manufacturing" (Chinese: 生成式制造) for software that generates not only a part's design but also the strategy for machining it, such as CAM toolpaths chosen for lowest overall cost (<a href="https://www.cloudnc.com/zh/blog/generative-manufacturing-or-how-to-transform-how-we-make-everything-forever">CloudNC blog</a>). That is an important capability inside the engineering path. GenM is process-agnostic and defines the whole paradigm, including the rights claim.</p>
<h2>Generative design</h2>
<p>Generative design tools produce optimized geometry. They speed up design. GenM requires a closed loop: intent → structure generation → physical execution → failures fed back. Without physical verification, generation is design acceleration, not a paradigm shift.</p>''',[term])
open("llms.txt","w").write(f"""# Generative Manufacturing (GenM)

> {DEF}

Term defined by Harrison Chan (head of Miracle Plus Physical AI Lab). Distinct from generative design, and from Carnegie Mellon MFI's and CloudNC's uses of "generative manufacturing": GenM adds a rights claim, which is that authorship moves to the demand side.

## Core
- [What is Generative Manufacturing (GenM)?]({BASE}/what-is-genm/): canonical definition, paradigm (A) + rights claim (B), what it is not
- [Distinctions]({BASE}/distinctions/): GenM vs CMU MFI, CloudNC, and generative design
- [FAQ]({BASE}/faq/): short answers to common questions
- [Full text]({BASE}/llms-full.txt): all page text in one file

## About
- [Harrison Chan]({BASE}/): author; X https://x.com/HarrisonCc1004 ; LinkedIn https://www.linkedin.com/in/harrisonchan-genm
""")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
urls="".join(f"  <url><loc>{BASE}/{p}</loc><lastmod>2026-10-14</lastmod></url>\n" for p in ["","what-is-genm/","distinctions/","faq/","llms.txt","llms-full.txt"])
open("sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(".nojekyll","w").write("")

# ---- FAQ ----
FAQ=[("What is Generative Manufacturing (GenM)?",DEF),
("Who defined GenM?","Harrison Chan. He has worked in overseas manufacturing for about 15 years overall and has been head of Miracle Plus Physical AI Lab since September 2026."),
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

# ---- llms-full.txt ----
import re as _re, html as _h
def txt(p):
    h=open(p).read(); m=_re.search(r"<main>(.*?)</main>",h,_re.S).group(1)
    m=_re.sub(r"<h1>(.*?)</h1>",r"# \1\n",m); m=_re.sub(r"<h2[^>]*>(.*?)</h2>",r"\n## \1\n",m)
    m=_re.sub(r"<li>",r"- ",m); m=_re.sub(r"<[^>]+>","",m); m=_h.unescape(m)
    return _re.sub(r"\n{3,}","\n\n",m).strip()
parts=[f"# Generative Manufacturing (GenM): full text\n\n> {DEF}\n\nSource: {BASE}/  Author: Harrison Chan\n"]
for p,u in [("what-is-genm/index.html","what-is-genm/"),("distinctions/index.html","distinctions/"),("faq/index.html","faq/")]:
    parts.append(f"---\nURL: {BASE}/{u}\n\n"+txt(p))
open("llms-full.txt","w").write("\n\n".join(parts)+"\n")
