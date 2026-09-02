#!/usr/bin/env python3
"""Generate the website and README from data/tools.json.

Every tool card is pre-rendered into static HTML so search engines index the
whole catalogue without executing JavaScript. The client script only filters
what is already in the document.
"""
import json
import html
import pathlib
import datetime
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "tools.json").read_text(encoding="utf-8"))
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)

SITE = "https://deepshah0308.github.io/awesome-intunetools/"
REPO = "https://github.com/Deepshah0308/awesome-intunetools"
OWNER = "Deepshah0308"
TITLE = "Awesome Intune Tools"
TAGLINE = "A curated directory of community tools, scripts and utilities for Microsoft Intune administrators."
TODAY = datetime.date.today().isoformat()

CATS = DATA["categories"]
TOOLS = DATA["tools"]
CAT_BY_ID = {c["id"]: c for c in CATS}
KIND_LABEL = {"repo": "Open source", "web": "Hosted tool", "guide": "Guide"}

LOGO = (
    '<svg viewBox="0 0 32 32" fill="none" aria-hidden="true" focusable="false">'
    '<path d="M16 2.6 27.5 9.3v13.4L16 29.4 4.5 22.7V9.3z" stroke="currentColor" '
    'stroke-width="2" stroke-linejoin="round"/>'
    '<path d="M11.5 13h9M11.5 16.5h9M11.5 20h5.5" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round"/></svg>'
)


def e(s):
    return html.escape(str(s), quote=True)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def tools_in(cid):
    return [t for t in TOOLS if t["category"] == cid]


def host(url):
    m = re.match(r"https?://([^/]+)", url)
    return m.group(1).replace("www.", "") if m else url


def masthead():
    return f"""<header class="top">
  <div class="wrap top-in">
    <a class="mark" href="index.html">{LOGO}<span>Awesome Intune Tools</span></a>
    <nav class="top-links" aria-label="Main">
      <a href="index.html#results">Browse tools</a>
      <a href="sponsor.html">Sponsor</a>
      <a href="{REPO}">GitHub</a>
      <a href="submit.html" class="cta">Submit a tool</a>
    </nav>
  </div>
</header>"""


def footer():
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h3>Awesome Intune Tools</h3>
        <p>{len(TOOLS)} community-built tools for Microsoft Intune administrators, kept current and link-checked weekly.</p>
      </div>
      <div>
        <h3>Contribute</h3>
        <ul>
          <li><a href="submit.html">Submit a tool</a></li>
          <li><a href="{REPO}/issues" rel="noopener">Report a broken link</a></li>
          <li><a href="{REPO}" rel="noopener">Source on GitHub</a></li>
        </ul>
      </div>
      <div>
        <h3>Support the project</h3>
        <ul>
          <li><a href="sponsor.html">Sponsorship options</a></li>
          <li><a href="https://github.com/sponsors/{OWNER}" rel="noopener">GitHub Sponsors</a></li>
        </ul>
      </div>
    </div>
    <p class="foot-base">Maintained by <a href="https://github.com/{OWNER}" rel="noopener">Deep Shah</a>.
    The list is licensed <a href="http://creativecommons.org/licenses/by/4.0/" rel="noopener license">CC BY 4.0</a>;
    each tool is licensed by its own author. Not affiliated with Microsoft.</p>
  </div>
</footer>"""


def head(title, desc, path, extra=""):
    url = SITE + ("" if path == "index.html" else path)
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Deep Shah">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(TITLE)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}og-image.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}og-image.svg">
<meta name="theme-color" content="#141B26">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Space+Grotesk:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
{extra}"""


def json_ld():
    items = [{
        "@type": "ListItem",
        "position": i,
        "item": {
            "@type": "SoftwareApplication",
            "name": t["name"],
            "description": t["desc"],
            "url": t["url"],
            "applicationCategory": "DeveloperApplication",
            "applicationSubCategory": CAT_BY_ID[t["category"]]["name"],
            "operatingSystem": "Windows, macOS, iOS, Android",
            "author": {"@type": "Person", "name": t["author"]},
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        },
    } for i, t in enumerate(TOOLS, 1)]

    blocks = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": TITLE,
         "url": SITE, "description": TAGLINE, "inLanguage": "en"},
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": TITLE,
         "url": SITE, "description": TAGLINE, "dateModified": TODAY,
         "license": "https://creativecommons.org/licenses/by/4.0/",
         "mainEntity": {"@type": "ItemList",
                        "name": f"{len(TOOLS)} Microsoft Intune tools",
                        "numberOfItems": len(TOOLS), "itemListElement": items}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question",
             "name": "What are the best free tools for Microsoft Intune administrators?",
             "acceptedAnswer": {"@type": "Answer", "text": (
                 f"This directory lists {len(TOOLS)} free and open-source Intune tools across device "
                 "management, troubleshooting, app packaging, Autopilot, reporting, security and "
                 "automation. Common starting points include Intune Debug Toolkit for client "
                 "troubleshooting, IntuneCD for configuration as code, OpenIntuneBaseline for a Windows "
                 "security baseline, and WinTuner for packaging Winget apps.")}},
            {"@type": "Question",
             "name": "How do I troubleshoot the Intune Management Extension?",
             "acceptedAnswer": {"@type": "Answer", "text": (
                 "Tools in the troubleshooting section parse IME logs into readable timelines. "
                 "Get-IntuneManagementExtensionDiagnostics builds an HTML timeline from the logs, "
                 "CMTraceOpen provides a modern log viewer, and Intune One Data Collector gathers the "
                 "full diagnostic set Microsoft support requests.")}},
            {"@type": "Question",
             "name": "How do I back up an Intune tenant configuration?",
             "acceptedAnswer": {"@type": "Answer", "text": (
                 "IntuneCD, IntuneBackupAndRestore and Microsoft365DSC export tenant configuration so it "
                 "can be stored in source control, compared between tenants, and restored. TenuVault and "
                 "TrustM365 add scheduled backups and configuration drift detection.")}},
            {"@type": "Question",
             "name": "How can I add a tool to this list?",
             "acceptedAnswer": {"@type": "Answer", "text": (
                 "Use the submission form on the website. It opens a pre-filled GitHub issue with the "
                 "tool details. Each submission is reviewed manually and, once approved, added to the "
                 "dataset that generates both the site and the README.")}},
        ]},
    ]
    return "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, separators=(",", ":"))}</script>'
        for b in blocks)


def card(t):
    c = CAT_BY_ID[t["category"]]
    text = f"{t['name']} {t['author']} {t['desc']} {c['name']}".lower()
    return f"""<article class="tool" data-cat="{e(t['category'])}" data-kind="{e(t['kind'])}" data-text="{e(text)}">
<h3><a href="{e(t['url'])}" rel="noopener">{e(t['name'])}</a></h3>
<p class="by">{e(t['author'])}</p>
<p class="desc">{e(t['desc'])}</p>
<p class="meta"><span class="kind kind-{e(t['kind'])}">{e(KIND_LABEL[t['kind']])}</span><span class="sep">/</span><span>{e(host(t['url']))}</span></p>
</article>"""


def build_index():
    sections = []
    for c in CATS:
        items = tools_in(c["id"])
        if not items:
            continue
        sections.append(f"""<section class="cat" id="{e(c['id'])}">
<header class="cat-head">
<h2>{e(c['name'])}</h2>
<p>{e(c['blurb'])}</p>
<span class="count">{len(items)}</span>
</header>
<div class="grid">
{chr(10).join(card(t) for t in items)}
</div>
</section>""")

    chips = "\n".join(
        f'<button class="chip" data-filter="{e(c["id"])}" type="button">{e(c["name"])}'
        f' <span>{len(tools_in(c["id"]))}</span></button>' for c in CATS)
    nav = "\n".join(
        f'<li><a href="#{e(c["id"])}">{e(c["name"])}</a><span>{len(tools_in(c["id"]))}</span></li>'
        for c in CATS)

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(f"{TITLE} \u2014 {len(TOOLS)} free tools and scripts for Microsoft Intune admins",
      f"A searchable directory of {len(TOOLS)} free, community-built Microsoft Intune tools: "
      "troubleshooting, app packaging, Autopilot, reporting, security baselines, macOS and Graph API automation.",
      "index.html", json_ld())}
</head>
<body>
<a class="skip" href="#results">Skip to the tools</a>
{masthead()}

<section class="hero">
  <div class="wrap">
    <h1>Find the right Intune tool without opening twelve tabs.</h1>
    <p class="lede">{len(TOOLS)} community-built tools, scripts and utilities for Microsoft Intune administrators, sorted into {len(CATS)} categories and checked weekly for broken links. Start typing to narrow the list.</p>

    <div class="search">
      <label for="q" class="sr">Search tools</label>
      <input id="q" type="search" autocomplete="off" spellcheck="false"
             placeholder="Try &quot;log&quot;, &quot;winget&quot;, &quot;macOS&quot; or &quot;backup&quot;">
      <p class="tally" id="tally" aria-live="polite">Showing all {len(TOOLS)} tools</p>
    </div>

    <div class="chips" role="group" aria-label="Filter by category">
      <button class="chip on" data-filter="all" type="button">Everything</button>
      {chips}
    </div>
  </div>
</section>

<div class="wrap layout">
  <aside class="rail">
    <h2 class="rail-h">Categories</h2>
    <ul>{nav}</ul>
    <p class="rail-note">Updated {TODAY}. Every link is verified by an automated weekly check.</p>
  </aside>

  <main id="results">
{chr(10).join(sections)}
    <p class="empty" id="empty" hidden>Nothing matches that. Try a shorter word, or <button type="button" id="reset">clear the filters</button>.</p>
  </main>
</div>

<section class="band">
  <div class="wrap">
    <h2>Know a tool that belongs here?</h2>
    <p class="sub">Submissions go through a short form and land as a GitHub issue for review. Community-built tools that solve a real Intune problem are welcome, whether or not you wrote them.</p>
    <p><a class="btn" href="submit.html">Submit a tool</a> <a class="btn btn-quiet" href="sponsor.html">Sponsor the project</a></p>
  </div>
</section>

{footer()}
<script src="app.js" defer></script>
</body>
</html>
"""
    (DOCS / "index.html").write_text(doc, encoding="utf-8")


def build_submit():
    opts = "\n".join(
        f'<option value="{e(c["id"])}">{e(c["name"])}</option>' for c in CATS)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(f"Submit a tool \u2014 {TITLE}",
      "Suggest a Microsoft Intune tool for the directory. Submissions are reviewed manually before "
      "being added to the list.", "submit.html")}
</head>
<body>
{masthead()}
<main class="wrap form-page">
  <h1>Submit a tool</h1>
  <p class="intro">Fill this in and it opens a pre-filled issue on GitHub for review. Nothing is published
  automatically. You need a free GitHub account so there is a record of who suggested what and somewhere
  to ask follow-up questions.</p>

  <form class="form" id="submitForm" novalidate>
    <div class="field">
      <label for="tool_name">Tool name</label>
      <input id="tool_name" name="tool_name" required maxlength="80" placeholder="IntuneCD">
      <p class="err" id="err_tool_name" hidden>Add the tool's name.</p>
    </div>

    <div class="field">
      <label for="tool_url">Link</label>
      <p class="hint">The canonical repository or project page, not a marketing landing page.</p>
      <input id="tool_url" name="tool_url" type="url" required placeholder="https://github.com/owner/repo">
      <p class="err" id="err_tool_url" hidden>Add a full link starting with https://</p>
    </div>

    <div class="field">
      <label for="author">Author or maintainer</label>
      <input id="author" name="author" required maxlength="80" placeholder="Name or GitHub handle">
      <p class="err" id="err_author" hidden>Add the author's name or handle.</p>
    </div>

    <div class="field">
      <label for="category">Category</label>
      <select id="category" name="category" required>
        <option value="">Choose one</option>
        {opts}
      </select>
      <p class="err" id="err_category" hidden>Pick the closest category.</p>
    </div>

    <div class="field">
      <label for="kind">Type</label>
      <select id="kind" name="kind" required>
        <option value="repo">Open source project</option>
        <option value="web">Hosted web tool</option>
        <option value="guide">Guide or blog post</option>
      </select>
    </div>

    <div class="field">
      <label for="description">What problem does it solve?</label>
      <p class="hint">One or two plain sentences. Describe the practical value, not the feature list.</p>
      <textarea id="description" name="description" required maxlength="400"
                placeholder="Backs up, documents and deploys Intune configuration from source control."></textarea>
      <p class="err" id="err_description" hidden>Add a short description.</p>
    </div>

    <div class="field">
      <label for="notes">Anything else? <span class="hint" style="display:inline">Optional</span></label>
      <textarea id="notes" name="notes" maxlength="400"
                placeholder="How it differs from similar tools already listed, whether you are the author, licensing notes."></textarea>
    </div>

    <button class="btn" type="submit">Review on GitHub</button>
    <p class="form-note">This opens GitHub with the issue already filled in. You still press submit there,
    so you can edit anything first.</p>
  </form>

  <h2 class="rail-h" style="margin-top:2.6rem;font-size:.95rem;color:var(--text)">What happens next</h2>
  <ol class="steps">
    <li><strong>Review.</strong> Every submission is checked by hand: the link has to resolve, the tool has to
    work on a current tenant, and it has to be documented well enough for someone else to adopt.</li>
    <li><strong>Decision.</strong> Approved tools are added to the dataset and appear on the site and in the
    README on the next build. If it is declined you get a reason on the issue, not a silent close.</li>
    <li><strong>Upkeep.</strong> Links are re-checked weekly. Entries that break get fixed or removed.</li>
  </ol>

  <p class="form-note">Prefer to skip the form? Open a pull request against
  <a href="{REPO}/blob/main/data/tools.json" rel="noopener">data/tools.json</a> directly.</p>
</main>
{footer()}
<script src="submit.js" defer></script>
</body>
</html>
"""
    (DOCS / "submit.html").write_text(doc, encoding="utf-8")


def build_sponsor():
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(f"Sponsorship \u2014 {TITLE}",
      "Support an independent, vendor-neutral directory of Microsoft Intune tools used by consultants, "
      "MSPs and in-house endpoint teams.", "sponsor.html")}
</head>
<body>
{masthead()}
<main class="wrap form-page">
  <h1>Sponsor this project</h1>
  <p class="intro">This directory is maintained independently and costs time rather than money: reviewing
  submissions, verifying links, testing tools, and keeping {len(TOOLS)} entries accurate as the Intune
  ecosystem shifts. Sponsorship pays for that time and keeps the list free and open.</p>

  <h2 style="font-size:1.2rem;margin:0 0 .6rem">Who reads this</h2>
  <p class="intro">Intune consultants, managed service providers, and in-house endpoint administrators \u2014
  people who evaluate and buy endpoint management tooling, or recommend it to the organisations they
  work for.</p>

  <div class="band-grid" style="margin:2.4rem 0">
    <div>
      <h3>Supporter</h3>
      <p>Your name or company listed in the README and in the site footer, with a link.</p>
    </div>
    <div>
      <h3>Project sponsor</h3>
      <p>Logo placement on the homepage and sponsor page, plus the README listing.</p>
    </div>
    <div>
      <h3>Custom</h3>
      <p>Something else in mind \u2014 a specific category, a piece of tooling, an integration? Get in touch
      and we can talk it through.</p>
    </div>
  </div>

  <h2 style="font-size:1.2rem;margin:0 0 .6rem">What sponsorship does not buy</h2>
  <p class="intro">Placement in the list itself. Tools are included on merit and every entry is reviewed the
  same way, whether a sponsor submitted it or not. Sponsors are shown as sponsors, in their own section,
  clearly labelled. A directory nobody trusts is not worth sponsoring, so this line stays firm.</p>

  <p style="margin-top:2rem">
    <a class="btn" href="https://github.com/sponsors/{OWNER}" rel="noopener">Sponsor on GitHub</a>
    <a class="btn btn-quiet" href="mailto:Deep030899@gmail.com?subject=Sponsoring%20Awesome%20Intune%20Tools">Email about sponsorship</a>
  </p>

  <h2 style="font-size:1.2rem;margin:2.8rem 0 .6rem">Current sponsors</h2>
  <p class="intro">None yet \u2014 this space is open. If your company builds endpoint tooling or serves Intune
  admins, you would be the first.</p>
</main>
{footer()}
</body>
</html>
"""
    (DOCS / "sponsor.html").write_text(doc, encoding="utf-8")


def build_readme():
    L = []
    L.append(f"# {TITLE}\n")
    L.append("[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)\n")
    L.append(f"{TAGLINE}\n")
    L.append(f"**Browse it as a searchable website: [{SITE.replace('https://', '').rstrip('/')}]({SITE})**\n")
    L.append(f"{len(TOOLS)} tools across {len(CATS)} categories, link-checked weekly. "
             f"[Submit a tool]({SITE}submit.html) \u00b7 [Sponsor the project]({SITE}sponsor.html)\n")

    L.append("## Contents\n")
    L.append("- [How to use this list](#how-to-use-this-list)")
    L.append("- [Contributing](#contributing)")
    L.append("- [Sponsorship](#sponsorship)")
    for c in CATS:
        L.append(f"- [{c['name']}](#{slug(c['name'])}) ({len(tools_in(c['id']))})")
    L.append("")

    L.append("## How to use this list\n")
    L.append("This is a directory for Intune consultants, MSPs, and in-house admins who want a working "
             "toolbox rather than more documentation. Pick two or three tools per use case, test them in a "
             "lab tenant, then standardise them into your own baseline toolkit.\n")
    L.append("**Auditing a tenant you have just inherited**  ")
    L.append("Start with Intune Management or Intune Inspector for a policy overview, Intune Assignment "
             "Checker for assignment hygiene, and IntuneCD or Microsoft365DSC to get the configuration into "
             "source control where you can diff it.\n")
    L.append("**Equipping a helpdesk**  ")
    L.append("Intune Debug Toolkit and Intune Device Troubleshooter cover day-to-day device work. "
             "CMTraceOpen and Get-IntuneManagementExtensionDiagnostics turn IME logs into something readable. "
             "IntuneDiag handles Entra join and PRT problems.\n")
    L.append("**Building an app packaging pipeline**  ")
    L.append("WinTuner or IntuneGet for Winget-sourced apps, PSAppDeployToolkit for anything needing user "
             "interaction, and Intune App Factory when you want it running unattended in a pipeline.\n")
    L.append("**Standing up a new tenant**  ")
    L.append("OpenIntuneBaseline gives you a defensible Windows starting point. IntuneHydrationKit fills a "
             "lab quickly. Add the platform baselines for macOS, iOS, and Android as needed.\n")

    L.append("## Contributing\n")
    L.append(f"The easiest route is the [submission form]({SITE}submit.html), which opens a pre-filled issue "
             "for review. You can also open a pull request directly.\n")
    L.append("### What belongs here\n")
    L.append("- Community-built tools, scripts, modules, or web apps that help manage, troubleshoot, secure, "
             "or automate Intune.")
    L.append("- Free or primarily community and open-source projects. Commercial SaaS with aggressive "
             "marketing is out of scope.")
    L.append("- Tools that are realistically usable: tested on modern tenants and documented well enough for "
             "someone else to adopt.\n")
    L.append("### Opening a pull request\n")
    L.append("The website and this README are both generated from [`data/tools.json`](data/tools.json), so "
             "that is the only file to edit. Do not edit `README.md` or anything in `docs/` by hand \u2014 those "
             "are overwritten on the next build.\n")
    L.append("```json")
    L.append("{")
    L.append('  "name": "Tool Name",')
    L.append('  "author": "Author or handle",')
    L.append('  "url": "https://github.com/owner/repo",')
    L.append('  "category": "troubleshooting",')
    L.append('  "kind": "repo",')
    L.append('  "desc": "One sentence on the problem it solves and why it is useful."')
    L.append("}")
    L.append("```\n")
    L.append("`category` must be one of the ids at the top of `data/tools.json`. `kind` is `repo` for source "
             "repositories, `web` for hosted tools, or `guide` for a written walkthrough.\n")
    L.append("### Guidelines\n")
    L.append("- Only suggest tools you have used or can reasonably recommend.")
    L.append("- Link to the canonical repository or project page, not a marketing landing page.")
    L.append("- Describe practical value in plain language. No vendor copy.")
    L.append("- Every link is checked automatically each week. Broken entries get fixed or removed.\n")

    L.append("## Sponsorship\n")
    L.append("This list is maintained independently. If your company builds endpoint tooling or serves Intune "
             f"admins, [sponsorship]({SITE}sponsor.html) supports the review and upkeep work that keeps it "
             "accurate.\n")
    L.append("Sponsorship does not buy placement in the list. Tools are included on merit and reviewed the "
             "same way regardless of who submitted them; sponsors appear in their own clearly labelled "
             "section.\n")

    for c in CATS:
        items = tools_in(c["id"])
        if not items:
            continue
        L.append(f"## {c['name']}\n")
        L.append(f"{c['blurb']}\n")
        for t in items:
            L.append(f"- **[{t['name']} \u2014 {t['author']}]({t['url']})** \u2014 {t['desc']}")
        L.append("")

    L.append("---\n")
    L.append("## License\n")
    L.append("[![Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)  ")
    L.append("This list is licensed under a Creative Commons Attribution 4.0 International License. "
             "The tools themselves are licensed by their respective authors. "
             "This project is not affiliated with Microsoft.")
    (ROOT / "README.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def build_seo():
    pages = [(SITE, "1.0"), (SITE + "submit.html", "0.8"), (SITE + "sponsor.html", "0.6")]
    pages += [(f"{SITE}#{c['id']}", "0.7") for c in CATS]
    body = "".join(
        f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod>"
        f"<changefreq>weekly</changefreq><priority>{p}</priority></url>" for u, p in pages)
    (DOCS / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + body + "</urlset>",
        encoding="utf-8")
    (DOCS / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "tools.json").write_text(json.dumps(DATA, indent=2), encoding="utf-8")


if __name__ == "__main__":
    build_readme()
    build_index()
    build_submit()
    build_sponsor()
    build_seo()
    print(f"Built {len(TOOLS)} tools in {len(CATS)} categories.")
