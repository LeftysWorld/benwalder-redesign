# Ben Walder Healing Arts: concept redesign

A redesign of benwalder.com built around one idea: a visitor in pain should see their problem, proof, a clear path and a booking button within seconds.

**Status: concept.** The site shows a "concept redesign" banner, is set to `noindex`, and uses visible dashed placeholders for anything that must come from Ben (prices, address, phone, credentials, review counts, client quotes, photos).

## Structure

- `content.py`: all page copy (homepage, 6 condition pages, 4 approach pages, Ten-Series, pricing, first visit, about, results, FAQ, herbal, contact, learn + 4 articles, 404)
- `build.py`: layout, components, icons, schema.org JSON-LD, `robots.txt`, `sitemap.xml`, `llms.txt`
- `static/`: CSS ("Rooted" brand system), JS (sticky mobile bar, nav, scroll-drawn signature line), images
- `site/`: generated output, committed so Render can publish it even without a build step. Run `python3 build.py` after editing and commit both.

## Build locally

```bash
python3 build.py
cd site && python3 -m http.server 8000
```

No dependencies beyond Python 3.

## Deploy (Render)

`render.yaml` defines a static site: build command `python3 build.py`, publish directory `site`. In Render: **New → Blueprint** (or **Static Site**) → pick this repo.

## Going live for real (once Ben approves)

1. Replace every placeholder in `build.py` (`PH` dict) and the bracketed items in `content.py`.
2. Replace sample testimonials with real client quotes, with written consent.
3. Swap photo placeholders for the shoot list (each placeholder names the exact shot).
4. Embed Jane App booking on `/pricing/#book` and the discovery-call calendar on `/contact/#call`; connect the forms.
5. Confirm Rolfing® certification before using the trademark.
6. In `build.py`: set `CONCEPT = False` and `SITE_URL` to the real domain. This removes the banner, allows indexing and opens `robots.txt` to search and AI crawlers.
