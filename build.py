#!/usr/bin/env python3
"""
Static site builder for the Ben Walder Healing Arts concept redesign.

    python3 build.py        -> writes the finished site to ./site

No dependencies beyond the Python standard library. Page content lives in
content.py; shared layout, icons and components live here.
"""
import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "site"
STATIC = ROOT / "static"

SITE_NAME = "Ben Walder Healing Arts"
SITE_URL = "https://benwalder-redesign.onrender.com"  # update once Render assigns the URL / custom domain
CONCEPT = True  # True = concept banner + noindex. Set False only when Ben approves and real details are in.

# Placeholders Ben fills in. Rendered with a dashed "ph" style so nobody mistakes them for real data.
PH = {
    "city": "[City]",
    "address": "[Street address], [City], CA [ZIP]",
    "phone": "(760) ___-____",
    "email": "hello@benwalder.com",
    "rating": "4.9",
    "reviews": "[XX]",
    "cert": "[Certification]",
    "first": "$___",
    "single": "$___",
    "series": "$____",
    "herbal": "$___",
}


def ph(key_or_text):
    """Visible placeholder span."""
    text = PH.get(key_or_text, key_or_text)
    return f'<span class="ph" title="Placeholder: replace with Ben\'s real detail">{html.escape(text)}</span>'


# --------------------------------------------------------------------------
# Icons — thin line icons drawn in the same style as the signature line
# --------------------------------------------------------------------------
ICONS = {
    "back": '<path d="M12 2.5c-2.6 3 2.6 5.2 0 8.3s2.6 5.3 0 8.4"/><path d="M9 5.5h6M9.2 9.5h5.6M9 13.5h6M9.2 17.5h5.6"/><path d="M12 19.2V21.5"/>',
    "scar": '<path d="M3.5 17c4-1.5 6.5-5.5 8.5-8s5.5-3 8.5-3"/><path d="M6.5 12.6l2.2 3.1M10 9.4l2.2 3.1M13.8 7l2 3.1"/>',
    "recovery": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.8v8.4M7.8 12h8.4"/>',
    "posture": '<circle cx="12" cy="4.5" r="2"/><path d="M12 6.5c-1.2 3.5 1.2 6.5 0 10.5"/><path d="M12 17l-3.2 4.5M12 17l3.2 4.5M7.5 10.5c1.5-.8 3-.9 4.5-.9s3 .1 4.5.9"/>',
    "stress": '<path d="M2.5 9c3-3.2 5.5 3.2 9.5 0s6.5 3.2 9.5 0"/><path d="M2.5 15c3-3.2 5.5 3.2 9.5 0s6.5 3.2 9.5 0"/>',
    "athlete": '<circle cx="15.5" cy="4" r="1.9"/><path d="M14.5 6.8l-3.2 5 3.6 2.8-1.9 6.4"/><path d="M11.3 11.8l-4.6.6M14.2 8.6l4.3 2.2M14.9 14.6l4.6 1.1"/>',
    "check": '<path d="M5 12.5l4.2 4.2L19 7"/>',
    "arrow": '<path d="M4 12h15M13.5 6.5L19 12l-5.5 5.5"/>',
    "star": '<path d="M12 3.5l2.6 5.4 5.9.8-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.8z"/>',
    "pin": '<path d="M12 21.5s-6.5-6.2-6.5-11.5a6.5 6.5 0 0113 0c0 5.3-6.5 11.5-6.5 11.5z"/><circle cx="12" cy="10" r="2.3"/>',
    "leaf": '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-14 14z"/><path d="M5 19c3-4 6-7 10-10"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 9.5h17M8 3v4M16 3v4"/>',
    "chat": '<path d="M4 5.5h16v10.5H9.5L5 20v-4H4z"/><path d="M8 9.5h8M8 12.5h5"/>',
    "badge": '<circle cx="12" cy="9" r="5.5"/><path d="M8.5 13.2L7 21l5-2.6 5 2.6-1.5-7.8"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "phone": '<path d="M5.5 3.5h3.2l1.6 4.2-2.1 1.4a11 11 0 006.7 6.7l1.4-2.1 4.2 1.6v3.2a2 2 0 01-2.2 2A16.5 16.5 0 013.5 5.7a2 2 0 012-2.2z"/>',
    "menu": '<path d="M4 7.5h16M4 12h16M4 16.5h16"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "hands": '<path d="M4 14c2-1 4-1.5 6-1.5h4.5a1.8 1.8 0 010 3.6H11"/><path d="M14.5 16.1l4.6-2.6a1.8 1.8 0 012 3l-6.6 4H7l-3-1.5"/><path d="M9 9.5c0-3 1.5-6 3-6s3 3 3 6"/>',
    "breath": '<path d="M3 9h11a3 3 0 10-3-3"/><path d="M3 13h15a3 3 0 11-3 3"/><path d="M3 17h7"/>',
    "layers": '<path d="M12 3.5l9 4.7-9 4.7-9-4.7z"/><path d="M3 12.3l9 4.7 9-4.7"/><path d="M3 16.3l9 4.7 9-4.7"/>',
    "head": '<path d="M7 19.5v-3a6.5 6.5 0 1110.5-5.1l1.6 3.1h-2v3h-3v2"/><path d="M10 9.5c1-.8 2.5-.8 3.5 0"/>',
    "spiral": '<path d="M12 12a1.5 1.5 0 101.5 1.5A3 3 0 1010.5 10.5a4.5 4.5 0 104.5 4.5 6 6 0 10-6-6 7.5 7.5 0 107.5 7.5"/>',
    "shield": '<path d="M12 3l7.5 3v5.5c0 4.6-3.2 8.3-7.5 9.5-4.3-1.2-7.5-4.9-7.5-9.5V6z"/><path d="M8.8 12l2.2 2.2 4.2-4.4"/>',
    "mail": '<rect x="3.5" y="5.5" width="17" height="13" rx="2"/><path d="M4 7l8 6 8-6"/>',
    "book": '<path d="M4 5.5c2.5-1 5.5-1 8 .5 2.5-1.5 5.5-1.5 8-.5v13c-2.5-1-5.5-1-8 .5-2.5-1.5-5.5-1.5-8-.5z"/><path d="M12 6v13"/>',
}


def icon(name, cls="", label=None):
    aria = f'role="img" aria-label="{html.escape(label)}"' if label else 'aria-hidden="true"'
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" {aria}>{ICONS[name]}</svg>')


ARROW = icon("arrow", "arrow")

LOGO_MARK = ('<svg class="brand-mark" viewBox="0 0 30 40" fill="none" stroke="currentColor" stroke-width="1.6" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M15 2c-4 4.2 4 7.4 0 12.2s4 7.6 0 12.6"/>'
             '<path d="M15 26.8c-1.6 4-5.2 6.6-10 10.2M15 26.8c1.6 4 5.2 6.6 10 10.2M15 26.8V38M15 31.5c-1.8 2.2-3.4 3.1-5.6 3.9M15 31.5c1.8 2.2 3.4 3.1 5.6 3.9"/>'
             '</svg>')

PHOTO_LINE = ('<svg class="photo-line" viewBox="0 0 100 120" fill="none" stroke="currentColor" stroke-width=".8" '
              'stroke-linecap="round" aria-hidden="true"><path d="M50 4c-12 12 12 22 0 36s12 24 0 38'
              'c-6 14-20 22-36 38M50 78c6 14 20 22 36 38M50 78v38"/></svg>')


def photo(caption, variant="", shape="arch", cls=""):
    """Art-directed photo placeholder. Every one names the exact shot to take."""
    shape_cls = {"arch": "photo--arch", "wide": "photo--wide", "square": "photo--square", "plain": ""}[shape]
    var_cls = f"photo--{variant}" if variant else ""
    return (f'<figure class="photo {shape_cls} {var_cls} {cls}" role="img" aria-label="Photo placeholder: {html.escape(caption)}">'
            f'{PHOTO_LINE}<figcaption><b>Photo to shoot</b>{html.escape(caption)}</figcaption></figure>')


# --------------------------------------------------------------------------
# Shared components
# --------------------------------------------------------------------------
def buttons(primary=("Book your first session", "/pricing/#book"), secondary=("Talk to Ben first, free", "/contact/#call"),
            light=False):
    sec_cls = "btn-light" if light else "btn-secondary"
    out = f'<div class="btn-row"><a class="btn btn-primary" href="{primary[1]}">{primary[0]}</a>'
    if secondary:
        out += f'<a class="btn {sec_cls}" href="{secondary[1]}">{secondary[0]}</a>'
    return out + "</div>"


def page_hero(eyebrow, h1, lede, crumbs=None, show_buttons=True, extra=""):
    bc = ""
    if crumbs:
        parts = ['<a href="/">Home</a>']
        for label, href in crumbs:
            parts.append(f'<a href="{href}">{label}</a>' if href else f'<span aria-current="page" style="margin:0;color:inherit">{label}</span>')
        bc = '<nav class="breadcrumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(parts) + '</nav>'
    btns = buttons() if show_buttons else ""
    return (f'<section class="page-hero"><div class="container">{bc}'
            f'<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lede">{lede}</p>{btns}{extra}</div></section>')


def checklist(items):
    lis = "".join(f'<li>{icon("check")}<span>{i}</span></li>' for i in items)
    return f'<ul class="checklist">{lis}</ul>'


def faq_block(faqs):
    items = []
    for q, a in faqs:
        items.append(f'<details><summary>{q}<span class="pm" aria-hidden="true"></span></summary>'
                     f'<div class="answer">{a}</div></details>')
    return '<div class="faq">' + "".join(items) + "</div>"


def testimonial(chip, quote, who="[Client name]", town="[Town]", feature=False):
    cls = "quote-card quote-card--feature" if feature else "quote-card"
    return (f'<figure class="{cls}"><div><span class="ph-note">Sample: replace with a real client quote (with consent)</span></div>'
            f'<span class="chip">{chip}</span><blockquote>{quote}</blockquote>'
            f'<figcaption class="quote-meta"><div><strong>{who}</strong><span>{town}</span></div>'
            f'<span class="stars" aria-label="5 out of 5 stars">★★★★★</span></figcaption></figure>')


def cta_final(h="You've lived with it long enough. Let's find out why.",
              text="Book a first session, or start with a free 15-minute call. No pressure, no long commitments."):
    return (f'<section class="section section--forest cta-final" data-thread="0.5" data-thread-y="0.25"><div class="container">'
            f'<span class="eyebrow">Ready when you are</span><h2>{h}</h2><p class="lede">{text}</p>'
            f'{buttons(light=True)}'
            f'<p class="small mt-32" style="color:rgba(246,241,234,.7)">{icon("pin", "", None).replace("<svg", "<svg style=\"width:18px;height:18px;display:inline-block;vertical-align:-3px;margin-right:6px\"")}'
            f'{ph("address")} &nbsp;·&nbsp; By appointment</p></div></section>')


def section_head(eyebrow, h2, lede="", center=False):
    c = " center" if center else ""
    l = f'<p class="lede{" center" if center else ""}">{lede}</p>' if lede else ""
    return f'<div class="section-head{c}"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{l}</div>'


# --------------------------------------------------------------------------
# Layout
# --------------------------------------------------------------------------
NAV = [
    ("Conditions", "/conditions/"),
    ("Approaches", "/approaches/"),
    ("Ten-Series", "/ten-series/"),
    ("Pricing", "/pricing/"),
    ("About", "/about/"),
]
MOBILE_NAV = NAV + [
    ("Your first visit", "/first-visit/"),
    ("Results", "/results/"),
    ("Herbal &amp; nutrition", "/herbal-nutrition/"),
    ("FAQ", "/faq/"),
    ("Learn", "/learn/"),
    ("Contact", "/contact/"),
]


def nav_html(current):
    links = []
    for label, href in NAV:
        cur = ' aria-current="page"' if current and current.startswith(href) else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    return "".join(links)


def brand_html(extra_cls=""):
    return (f'<a class="brand {extra_cls}" href="/" aria-label="{SITE_NAME}, home">{LOGO_MARK}'
            f'<span class="brand-text"><span class="brand-name">Ben Walder</span>'
            f'<span class="brand-sub">Healing Arts</span></span></a>')


def business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "HealthAndBeautyBusiness",
        "@id": SITE_URL + "/#business",
        "name": SITE_NAME,
        "url": SITE_URL + "/",
        "description": ("Structural Integration, manual therapy, craniosacral and visceral work, plus herbal and "
                        "nutritional consultations for chronic pain, old injuries and post-surgical recovery in "
                        "North County San Diego."),
        "telephone": "[PHONE]",
        "email": PH["email"],
        "address": {"@type": "PostalAddress", "streetAddress": "[STREET]", "addressLocality": "[CITY]",
                    "addressRegion": "CA", "postalCode": "[ZIP]", "addressCountry": "US"},
        "areaServed": ["North County San Diego", "San Diego County"],
        "priceRange": "$$",
        "founder": {"@id": SITE_URL + "/about/#ben"},
        "knowsAbout": ["Structural Integration", "Rolfing", "Craniosacral therapy", "Visceral manipulation",
                       "Neurovascular manipulation", "Herbalism", "Nutrition", "Chronic pain", "Fascia"],
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "description": "By appointment"},
    }


def person_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": SITE_URL + "/about/#ben",
        "name": "Ben Walder",
        "jobTitle": "Structural Integration practitioner and herbalist",
        "worksFor": {"@id": SITE_URL + "/#business"},
        "url": SITE_URL + "/about/",
        "knowsAbout": ["Structural Integration", "Manual therapy", "Craniosacral therapy",
                       "Visceral manipulation", "Herbal medicine", "Nutrition"],
    }


def faq_schema(faqs):
    import re
    def strip(s):
        return re.sub(r"<[^>]+>", "", s).strip()
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": strip(q),
                        "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs],
    }


def breadcrumb_schema(path, title):
    if path == "/":
        return None
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"}]
    parts = [p for p in path.strip("/").split("/") if p]
    acc = ""
    for i, part in enumerate(parts, start=2):
        acc += "/" + part
        name = title if i == len(parts) + 1 else part.replace("-", " ").title()
        items.append({"@type": "ListItem", "position": i, "name": name, "item": SITE_URL + acc + "/"})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def layout(page):
    path = page["path"]
    title = page["title"]
    full_title = title if title.endswith(SITE_NAME) else f"{title} | {SITE_NAME}"
    desc = page["description"]
    canonical = SITE_URL + path

    schemas = [business_schema()]
    if path == "/" or path == "/about/":
        schemas.append(person_schema())
    if page.get("faqs"):
        schemas.append(faq_schema(page["faqs"]))
    bc = breadcrumb_schema(path, page.get("crumb", title))
    if bc:
        schemas.append(bc)
    schemas += page.get("schema", [])
    schema_html = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)

    robots = '<meta name="robots" content="noindex, nofollow">' if CONCEPT else '<meta name="robots" content="index, follow">'
    banner = ('<div class="concept-banner" role="note"><strong>Concept redesign.</strong> Not the official Ben Walder '
              'Healing Arts website. Highlighted items are placeholders for Ben\'s real details.</div>') if CONCEPT else ""

    mobile_links = "".join(f'<li><a href="{h}">{l}{ARROW}</a></li>' for l, h in MOBILE_NAV)

    return f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#F6F1EA">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/static/img/og-image.png">
<meta property="og:image:alt" content="Ben Walder Healing Arts: lasting relief for chronic pain and old injuries in North County San Diego">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/static/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,400..600,0..100;1,9..144,400..600,0..100&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/css/styles.css">
{schema_html}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{banner}
<header class="site-header">
  <div class="container header-inner">
    {brand_html()}
    <nav class="nav" aria-label="Main">{nav_html(path)}</nav>
    <div class="header-actions">
      <a class="btn btn-primary btn-sm header-book" href="/pricing/#book">Book</a>
      <button class="nav-toggle" type="button" data-nav-open aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">{icon("menu")}</button>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobile-nav" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mobile-nav-top">{brand_html()}<button class="nav-toggle" type="button" data-nav-close aria-label="Close menu" style="display:inline-flex">{icon("close")}</button></div>
  <ul>{mobile_links}</ul>
  <a class="btn btn-primary" href="/pricing/#book">Book your first session</a>
  <a class="btn btn-secondary" href="/contact/#call">Talk to Ben first, free</a>
</div>
<main id="main">
{page["body"]}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        {brand_html()}
        <p>Structural Integration, manual therapy and herbal care for chronic pain, old injuries and recovery in North County San Diego.</p>
        <p>{ph("address")}<br>By appointment</p>
      </div>
      <div><h4>Help with</h4><ul>
        <li><a href="/conditions/chronic-back-neck-pain/">Chronic back &amp; neck pain</a></li>
        <li><a href="/conditions/old-injuries-scar-tissue/">Old injuries &amp; scar tissue</a></li>
        <li><a href="/conditions/surgery-accident-recovery/">Surgery &amp; accident recovery</a></li>
        <li><a href="/conditions/posture-restricted-movement/">Posture &amp; movement</a></li>
        <li><a href="/conditions/stress-tension/">Stress &amp; tension</a></li>
        <li><a href="/conditions/athletes/">Athletes &amp; surfers</a></li>
      </ul></div>
      <div><h4>The practice</h4><ul>
        <li><a href="/ten-series/">The Ten-Series</a></li>
        <li><a href="/approaches/">Approaches</a></li>
        <li><a href="/herbal-nutrition/">Herbal &amp; nutrition</a></li>
        <li><a href="/first-visit/">Your first visit</a></li>
        <li><a href="/results/">Results</a></li>
        <li><a href="/learn/">Learn</a></li>
      </ul></div>
      <div><h4>Get in touch</h4><ul>
        <li><a href="/pricing/#book">Book online</a></li>
        <li><a href="/contact/">{ph("phone")}</a></li>
        <li><a href="mailto:{PH['email']}">{PH['email']}</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/contact/">Contact &amp; location</a></li>
      </ul></div>
    </div>
    <div class="footer-legal">
      <p class="mb-0">Bodywork and herbal consultations are educational and supportive. They are not a substitute for medical diagnosis or treatment, and Ben works alongside your medical care.</p>
      <p class="mb-0">© 2026 {SITE_NAME}.{' Concept redesign, not the official site.' if CONCEPT else ''}</p>
    </div>
  </div>
</footer>
<div class="sticky-bar" aria-label="Quick actions">
  <a class="btn btn-primary" href="/pricing/#book">Book a session</a>
  <a class="btn btn-secondary" href="/contact/#call">{icon("phone").replace('<svg', '<svg style="width:18px;height:18px"')}Call</a>
</div>
<script src="/static/js/main.js" defer></script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------
def write_static_extras(pages):
    if CONCEPT:
        robots = "# Concept preview: keep out of search engines until Ben approves.\nUser-agent: *\nDisallow: /\n"
    else:
        robots = ("User-agent: *\nAllow: /\n\n"
                  "# AI search crawlers are welcome\nUser-agent: GPTBot\nAllow: /\n"
                  "User-agent: OAI-SearchBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\n"
                  "User-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\n"
                  f"Sitemap: {SITE_URL}/sitemap.xml\n")
    (OUT / "robots.txt").write_text(robots)

    urls = "\n".join(f"  <url><loc>{SITE_URL}{p['path']}</loc></url>" for p in pages if p["path"] != "/404/")
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')

    lines = [f"# {SITE_NAME}", "",
             "> Structural Integration (often called Rolfing), integrative manual therapy, craniosacral, visceral and "
             "neurovascular work, plus herbal and nutritional consultations, for people in North County San Diego "
             "with chronic pain, old injuries, post-surgical or post-accident recovery, posture problems and stress "
             "held in the body. Practitioner: Ben Walder, about 15 years of study and practice. By appointment.", "",
             "## Key pages"]
    for p in pages:
        if p["path"] in ("/404/",):
            continue
        lines.append(f"- [{p['title']}]({SITE_URL}{p['path']}): {p['description']}")
    (OUT / "llms.txt").write_text("\n".join(lines) + "\n")


def build():
    from content import PAGES  # noqa: E402
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(STATIC, OUT / "static")
    for page in PAGES:
        target = OUT / "404.html" if page["path"] == "/404/" else OUT / page["path"].strip("/") / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(layout(page))
    write_static_extras(PAGES)
    print(f"Built {len(PAGES)} pages into {OUT}")


if __name__ == "__main__":
    build()
