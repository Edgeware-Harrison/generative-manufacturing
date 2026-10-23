# Builds essays/<slug>/ from essays_src/<slug>.md (verbatim approved text). exec'd from build.py.
# Per-essay extras (figure, cross-links, citations) live in ESSAY_EXTRA, keyed by slug.
import re as _r, html as _hh
def _inline(t):
    t=_hh.escape(t,quote=False)
    t=_r.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",t)
    t=_r.sub(r"(?<![*\w])\*([^*\n]+?)\*(?![*\w])",r"<em>\1</em>",t)
    return _r.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)",lambda m:f'<a href="{m.group(2)}">{m.group(1)}</a>',t)
def md2html(md):
    md=_r.sub(r"\A---\n.*?\n---\n","",md,flags=_r.S)
    out=[];title=None;lst=[]
    def flush():
        if lst: out.append("<ul>\n"+"\n".join(f"<li>{_inline(x)}</li>" for x in lst)+"\n</ul>"); lst.clear()
    for blk in [b.strip() for b in md.split("\n\n") if b.strip()]:
        lines=blk.split("\n")
        if all(l.startswith("- ") for l in lines): lst.extend(l[2:] for l in lines); continue
        flush()
        if blk.startswith("# "): title=blk[2:]; out.append(f"<h1>{_inline(title)}</h1>")
        elif blk.startswith("## "): out.append(f'<h2 id="{_r.sub(r"[^a-z0-9]+","-",blk[3:].lower()).strip("-")}">{_inline(blk[3:])}</h2>')
        else: out.append(f"<p>{_inline(' '.join(lines))}</p>")
    flush(); return title,out
P1_ALT=("Diagram: between the need and the factory sits a chain of human translators. Six boxes in a row, "
         "Need (in the requester's own words), Spec (someone rewrites it), Drawing (someone draws it), Parts list "
         "(someone breaks it down), Route (someone plans the steps) and Quote (someone prices it), with an arrow "
         "marked loss at each hand-off. Each hand-off loses something. A compiler for physical things would have to replace this chain.")
P2_ALT=("Diagram: Where the drawing sits. Same job, different front door. Left, drawing at the front door: the person with the need "
         "has to supply a drawing or hire someone who can; the drawing is the gate (no drawing, no custom work); the shop quotes, plans and builds from it. "
         "Right, intent at the front door: the person states intent (what it must do, where it goes, what it can't exceed); the system produces "
         "the drawing, parts list and plan in the middle; the shop makes it; a commitment states what was checked against the intent, and by whom. "
         "The test: can making start without a drawing or a catalog item?")
ESSAY_EXTRA={
 P1_SLUG:{"img":"translator-chain.png","alt":P1_ALT,"after":"<p>Follow a custom order","display_date":"19 October 2026",
   "links":[("p1_li_article","LinkedIn article"),("p1_li_post","LinkedIn post"),("p1_x","X thread")],
   "keywords":"Generative Manufacturing (GenM), compiler for physical things","same":["p1_li_article"],
   "citation":["arxiv","cloudnc","tnw_atomic","atomic"]},
 P2_SLUG:{"img":"drawing-vs-intent.png","alt":P2_ALT,"after":"<p>Drawings are the language factories need.","display_date":"22 October 2026",
   "links":[("p2_li_article","LinkedIn article"),("p2_li_post","LinkedIn post"),("p2_x","X thread")],
   "keywords":"Generative Manufacturing (GenM), intent, drawings, demand-side authorship","same":["p2_li_article"],
   "citation":[]},
}
for e in ESSAYS:
    x=ESSAY_EXTRA[e["slug"]]
    src=open(f"essays_src/{e['slug']}.md").read()
    fm=dict(_r.findall(r'^(\w+): "(.*)"$',src.split("\n---\n")[0],_r.M))
    title,blocks=md2html(src)
    assert title==e["title"]==fm["title"] and fm["description"]==e["summary"]
    assert blocks[-1]==f"<p>{DEF}</p>", "locked sentence must be last"
    url=U("essays/"+e["slug"]); img=url+x["img"]
    fig=(f'<figure><img src="{img}" alt="{_hh.escape(x["alt"])}" width="1600" height="900" loading="lazy" '
         f'style="max-width:100%;height:auto;border:1px solid #ddd"></figure>')
    i=next(k for k,b in enumerate(blocks) if b.startswith(x["after"])); blocks.insert(i+1,fig)
    if e["slug"]==P1_SLUG:
        j=next(k for k,b in enumerate(blocks) if b.startswith("<p>Also on") or b.startswith("<p>Reference page:") or b==f"<p>{DEF}</p>")
        blocks.insert(j,"<h2 id=\"the-short-version\">The short version, in 57 seconds</h2>\n"+VIDEO_HTML)
    also='<p>Also on LinkedIn / X: '+' · '.join(f'<a href="{S[k]}">{n}</a>' for k,n in x["links"])+'</p>'
    ref=next((k for k,b in enumerate(blocks) if b.startswith("<p>Reference page:")),len(blocks)-1)
    blocks.insert(ref,also)
    blocks.insert(1,f'<p><small>Harrison Chan · <time datetime="{e["date"]}">{x["display_date"]}</time> · Part of <a href="{U("essays")}">Essays</a>. Definition: <a href="{U("what-is-genm")}">What is Generative Manufacturing (GenM)?</a></small></p>')
    art={"@context":"https://schema.org","@type":"Article","@id":url+"#article","headline":e["title"],"description":e["summary"],
         "url":url,"mainEntityOfPage":url,"image":img,"datePublished":e["date"],"dateModified":e["date"],"inLanguage":"en",
         "author":{"@type":"Person","@id":f"{BASE}/#person","name":"Harrison Chan","url":f"{BASE}/"},
         "publisher":{"@id":f"{BASE}/#person"},"about":{"@id":term["@id"]},"isPartOf":{"@id":U("essays")+"#page"},
         "keywords":x["keywords"],
         "sameAs":[S[k] for k in x["same"]],
         **({"citation":[S[k] for k in x["citation"]]} if x["citation"] else {})}
    page("essays/"+e["slug"],f'{e["title"]} | Harrison Chan',e["summary"],"\n".join(blocks),
         [art]+([video_obj] if e["slug"]==P1_SLUG else [])+[crumbs([("Home",U("")),("Essays",U("essays")),(e["title"],url)])],[HOME,("Essays",U("essays")),(e["title"],url)],image=img)
