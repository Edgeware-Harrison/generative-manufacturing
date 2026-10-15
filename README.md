# generative-manufacturing: Generative Manufacturing (GenM) canonical site

Static files, no build step. Nothing has been pushed or published yet.

## Files
- `index.html`: home and about (Person JSON-LD)
- `what-is-genm/index.html`: canonical definition (DefinedTerm + Person JSON-LD)
- `distinctions/index.html`: credit to earlier uses of the phrase (CMU MFI + arXiv 2409.03089, CloudNC), with dates
- `genm-vs-adjacent-terms/index.html`: side-by-side comparison with adjacent terms
- `glossary/index.html`: glossary (DefinedTermSet, id `https://whatisgenm.com/#glossary`)
- `timeline/index.html`: dated, sourced events; three author-stated rows
- `essays/index.html`: essay archive (placeholder; `noindex`, not in sitemap or llms files until the first post)
- `faq/index.html`: FAQ (FAQPage JSON-LD)
- `schema/definedterm.jsonld`, `schema/definedtermset.jsonld`, `schema/person.jsonld`, `schema/faqpage.jsonld`: standalone copies
- `llms.txt`, `llms-full.txt`, `robots.txt`, `sitemap.xml`, `.nojekyll`

## Base URL
Every absolute URL uses `https://whatisgenm.com` (the `BASE` value in `build.py`). To change it, edit `BASE` and run `python3 build.py`. `build.py` regenerates every page, the schema files, llms.txt, llms-full.txt and sitemap.xml. Edit content there, not in the generated HTML.

## Deploy to GitHub Pages
1. Create the repo `Edgeware-Harrison/generative-manufacturing` and push these files to `main`, with the site at the repo root. `CNAME` (containing `whatisgenm.com`) must be included.
2. Go to Settings → Pages → Source: "Deploy from a branch", then choose `main` / `/ (root)`.
3. Settings → Pages → Custom domain: enter `whatisgenm.com` and save. GitHub recommends verifying the domain first under your account's Settings → Pages → "Add a domain", which uses a TXT record.
4. Add the DNS records below at the registrar.
5. Once DNS resolves and the certificate is issued (this can take up to 24 h), tick **Enforce HTTPS** in Settings → Pages. Don't skip this step.
6. Submit `https://whatisgenm.com/sitemap.xml` in Google Search Console and Bing Webmaster Tools.

<!-- DNS-NOTES-START -->
### DNS for whatisgenm.com (GitHub Pages)
| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | edgeware-harrison.github.io |

Check with `dig whatisgenm.com +noall +answer` and `dig www.whatisgenm.com +noall +answer`. GitHub redirects `www` to the apex. Before the domain is set, the site would be at edgeware-harrison.github.io/generative-manufacturing/.
<!-- DNS-NOTES-END -->

## Validate
`python3 check_links.py` makes a live HTTP check of every URL in `sources.json` (network needed). To publish the first essay: add it to `ESSAYS` in `build.py`, drop `noindex=True` on the essays page, add it to the sitemap and llms lists, rebuild.

`python3 validate.py` parses all HTML and embedded or standalone JSON-LD.
For a final check after deploying, use https://validator.schema.org and https://search.google.com/test/rich-results.

## Language
The site is English only for now. There is no Chinese page and there are no hreflang links.

## Guardrails
- Use the locked definition sentence verbatim and don't edit it.
- About 15 years refers to overseas manufacturing overall. The Surabaya furniture ODM ran 2010–2020 and is unnamed. Never say "15 years" about the factory.
- Edgeware: no delivery, pilot, or customer claims. No price or sales CTA.
