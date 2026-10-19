# Builds essays/<slug>/ from essays_src/<slug>.md (verbatim approved text). exec'd from build.py.
import re as _r, html as _hh
def _inline(t):
    t=_hh.escape(t,quote=False)
    t=_r.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",t)
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
for e in ESSAYS:
    src=open(f"essays_src/{e['slug']}.md").read()
    fm=dict(_r.findall(r'^(\w+): "(.*)"$',src.split("\n---\n")[0],_r.M))
    title,blocks=md2html(src)
    assert title==e["title"]==fm["title"] and fm["description"]==e["summary"]
    assert blocks[-1]==f"<p>{DEF}</p>", "locked sentence must be last"
    url=U("essays/"+e["slug"]); img=url+"translator-chain.png"
    alt=("Diagram: between the need and the factory sits a chain of human translators. Six boxes in a row, "
         "Need (in the requester's own words), Spec (someone rewrites it), Drawing (someone draws it), Parts list "
         "(someone breaks it down), Route (someone plans the steps) and Quote (someone prices it), with an arrow "
         "marked loss at each hand-off. Each hand-off loses something. A compiler for physical things would have to replace this chain.")
    fig=(f'<figure><img src="{img}" alt="{_hh.escape(alt)}" width="1600" height="900" loading="lazy" '
         f'style="max-width:100%;height:auto;border:1px solid #ddd"></figure>')
    i=next(k for k,b in enumerate(blocks) if b.startswith("<p>Follow a custom order")); blocks.insert(i+1,fig)
    also=(f'<p>Also on LinkedIn / X: <a href="{S["p1_li_article"]}">LinkedIn article</a> · '
          f'<a href="{S["p1_li_post"]}">LinkedIn post</a> · <a href="{S["p1_x"]}">X thread</a></p>')
    blocks.insert(len(blocks)-1,also)
    blocks.insert(1,f'<p><small>Harrison Chan · <time datetime="{e["date"]}">19 October 2026</time> · Part of <a href="{U("essays")}">Essays</a>. Definition: <a href="{U("what-is-genm")}">What is Generative Manufacturing (GenM)?</a></small></p>')
    art={"@context":"https://schema.org","@type":"Article","@id":url+"#article","headline":e["title"],"description":e["summary"],
         "url":url,"mainEntityOfPage":url,"image":img,"datePublished":e["date"],"dateModified":e["date"],"inLanguage":"en",
         "author":{"@type":"Person","@id":f"{BASE}/#person","name":"Harrison Chan","url":f"{BASE}/"},
         "publisher":{"@id":f"{BASE}/#person"},"about":{"@id":term["@id"]},"isPartOf":{"@id":U("essays")+"#page"},
         "keywords":"Generative Manufacturing (GenM), compiler for physical things",
         "sameAs":[S["p1_li_article"]],
         "citation":[S["arxiv"],S["cloudnc"],S["tnw_atomic"],S["atomic"]]}
    page("essays/"+e["slug"],f'{e["title"]} | Harrison Chan',e["summary"],"\n".join(blocks),
         [art,crumbs([("Home",U("")),("Essays",U("essays")),(e["title"],url)])],[HOME,("Essays",U("essays")),(e["title"],url)],image=img)
