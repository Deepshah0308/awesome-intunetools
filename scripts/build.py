#!/usr/bin/env python3
"""Generate the website and README from data/tools.json.

Everything is pre-rendered to static HTML so search engines index each tool
without executing JavaScript. The client-side script only filters what is
already in the document.
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
TITLE = "Awesome Intune Tools"
TAGLINE = "A curated directory of community tools, scripts and utilities for Microsoft Intune administrators."
TODAY = datetime.date.today().isoformat()

CATS = DATA["categories"]
TOOLS = DATA["tools"]
CAT_BY_ID = {c["id"]: c for c in CATS}

KIND_LABEL = {
    "repo": "Open source",
    "web": "Hosted tool",
    "guide": "Guide",
}


def e(s):
    return html.escape(str(s), quote=True)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def tools_in(cid):
    return [t for t in TOOLS if t["category"] == cid]


def host(url):
    m = re.match(r"https?://([^/]+)", url)
    return m.group(1).replace("www.", "") if m else url


def build_readme():
    L = []
    L.append(f"# {TITLE}\n")
    L.append(
        "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]"
        "(https://github.com/sindresorhus/awesome)\n"
    )
    L.append(f"{TAGLINE}\n")
    L.append(f"**Browse it as a searchable website: [{SITE.replace('https://', '').rstrip('/')}]({SITE})**\n")
    L.append(f"{len(TOOLS)} tools across {len(CATS)} categories. Contributions welcome - see [Contributing](#contributing).\n")

    L.append("## Contents\n")
    L.append("- [How to use this list](#how-to-use-this-list)")
    L.append("- [Contributing](#contributing)")
    for c in CATS:
        L.append(f"- [{c['name']}](#{slug(c['name'])}) ({len(tools_in(c['id']))})")
    L.append("")

    L.append("## How to use this list\n")
    L.append(
        "This is a directory for Intune consultants, MSPs, and in-house admins who want a working "
        "toolbox rather than more documentation. Pick two or three tools per use case, test them in a "
        "lab tenant, then standardise them into your own baseline toolkit.\n"
    )
    L.append("**Auditing a tenant you have just inherited**  ")
    L.append(
        "Start with Intune Management or Intune Inspector for a policy overview, Intune Assignment "
        "Checker for assignment hygiene, and IntuneCD or Microsoft365DSC to get the configuration into "
        "source control where you can diff it.\n"
    )
    L.append("**Equipping a helpdesk**  ")
    L.append(
        "Intune Debug Toolkit and Intune Device Troubleshooter cover day-to-day device work. "
        "CMTraceOpen and Get-IntuneManagementExtensionDiagnostics turn IME logs into something readable. "
        "IntuneDiag handles Entra join and PRT problems.\n"
    )
    L.append("**Building an app packaging pipeline**  ")
    L.append(
        "WinTuner or IntuneGet for Winget-sourced apps, PSAppDeployToolkit for anything needing user "
        "interaction, and Intune App Factory when you want the whole thing running unattended in a pipeline.\n"
    )
    L.append("**Standing up a new tenant**  ")
    L.append(
        "OpenIntuneBaseline gives you a defensible Windows starting point. IntuneHydrationKit fills a lab "
        "quickly. Add the platform baselines for macOS, iOS, and Android as needed.\n"
    )

    L.append("## Contributing\n")
    L.append("Contributions from the Intune community are very welcome.\n")
    L.append("### What belongs here\n")
    L.append("- Community-built tools, scripts, modules, or web apps that help manage, troubleshoot, secure, or automate Intune.")
    L.append("- Free or primarily community and open-source projects. Commercial SaaS with aggressive marketing is out of scope.")
    L.append("- Tools that are realistically usable: tested on modern tenants and documented well enough for someone else to adopt.\n")
    L.append("### How to contribute\n")
    L.append(
        "The website and this README are both generated from [`data/tools.json`](data/tools.json), so that "
        "is the only file you need to edit. Do not edit `README.md` or anything in `docs/` by hand - your "
        "changes will be overwritten on the next build.\n"
    )
    L.append("1. Fork the repository and create a branch, for example `add-my-tool`.")
    L.append("2. Add an entry to the `tools` array in `data/tools.json`:\n")
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
    L.append(
        "`category` must be one of the ids listed at the top of `data/tools.json`. `kind` is `repo` for "
        "source repositories, `web` for hosted tools, or `guide` for a blog post or written walkthrough.\n"
    )
    L.append("3. Open a pull request explaining what you are adding. If it overlaps with something already listed, say what is different about it.\n")
    L.append("### Guidelines\n")
    L.append("- Only suggest tools you have used or can reasonably recommend.")
    L.append("- Link to the canonical repository or project page, not a marketing landing page.")
    L.append("- Describe practical value in plain language. No vendor copy.")
    L.append("- Every link in this list is automatically checked. Entries whose links break will be fixed or removed.\n")

    for c in CATS:
        items = tools_in(c["id"])
        if not items:
            continue
        L.append(f"## {c['name']}\n")
        L.append(f"{c['blurb']}\n")
        for t in items:
            L.append(f"- **[{t['name']} - {t['author']}]({t['url']})** - {t['desc']}")
        L.append("")

    L.append("---\n")
    L.append("## License\n")
    L.append("[![Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)  ")
    L.append(
        "This list is licensed under a Creative Commons Attribution 4.0 International License. "
        "The tools themselves are licensed by their respective authors."
    )
    (ROOT / "README.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def json_ld():
    items = []
    for i, t in enumerate(TOOLS, 1):
        items.append({
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
        })
    blocks = [
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": TITLE,
            "url": SITE,
            "description": TAGLINE,
            "inLanguage": "en",
        },
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": TITLE,
            "url": SITE,
            "description": TAGLINE,
            "dateModified": TODAY,
            "license": "https://creativecommons.org/licenses/by/4.0/",
            "mainEntity": {
                "@context": "https://schema.org",
                "@type": "ItemList",
                "name": f"{len(TOOLS)} Microsoft Intune tools",
                "numberOfItems": len(TOOLS),
                "itemListElement": items,
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "What are the best free tools for Microsoft Intune administrators?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": (
                            "This directory lists " + str(len(TOOLS)) + " free and open-source Intune tools "
                            "across device management, troubleshooting, app packaging, Autopilot, reporting, "
                            "security and automation. Widely used starting points include Intune Debug Toolkit "
                            "for client troubleshooting, IntuneCD for configuration as code, OpenIntuneBaseline "
                            "for a Windows security baseline, and WinTuner for packaging Winget apps."
                        ),
                    },
                },
                {
                    "@type": "Question",
                    "name": "How do I troubleshoot the Intune Management Extension?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": (
                            "Tools in the troubleshooting section parse IME logs into readable timelines. "
                            "Get-IntuneManagementExtensionDiagnostics builds an HTML timeline from the logs, "
                            "CMTraceOpen provides a modern log viewer, and Intune One Data Collector gathers "
                            "the full diagnostic set Microsoft support requests."
                        ),
                    },
                },
                {
                    "@type": "Question",
                    "name": "How do I back up an Intune tenant configuration?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": (
                            "IntuneCD, IntuneBackupAndRestore and Microsoft365DSC export tenant configuration "
                            "so it can be stored in source control, compared between tenants, and restored. "
                            "TenuVault and TrustM365 add scheduled backups and configuration drift detection."
                        ),
                    },
                },
            ],
        },
    ]
    return "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, separators=(",", ":"))}</script>'
        for b in blocks
    )


def card(t):
    c = CAT_BY_ID[t["category"]]
    blob = (t["name"] + " " + t["author"] + " " + t["desc"] + " " + c["name"]).lower()
    return (
        f'<article class="tool" data-cat="{e(t["category"])}" data-kind="{e(t["kind"])}" data-text="{e(blob)}">\n'
        f'<h3><a href="{e(t["url"])}" rel="noopener">{e(t["name"])}</a></h3>\n'
        f'<p class="by">{e(t["author"])}</p>\n'
        f'<p class="desc">{e(t["desc"])}</p>\n'
        f'<p class="meta"><span class="kind kind-{e(t["kind"])}">{e(KIND_LABEL[t["kind"]])}</span>'
        f'<span class="src">{e(host(t["url"]))}</span></p>\n'
        f'</article>'
    )


def build_site():
    sections = []
    for c in CATS:
        items = tools_in(c["id"])
        if not items:
            continue
        cards = "\n".join(card(t) for t in items)
        sections.append(
            f'<section class="cat" id="{e(c["id"])}" data-cat="{e(c["id"])}">\n'
            f'<header class="cat-head">\n<h2>{e(c["name"])}</h2>\n'
            f'<p>{e(c["blurb"])}</p>\n<span class="count">{len(items)}</span>\n</header>\n'
            f'<div class="grid">\n{cards}\n</div>\n</section>'
        )

    chips = "\n".join(
        f'<button class="chip" data-filter="{e(c["id"])}" type="button">{e(c["name"])} <span>{len(tools_in(c["id"]))}</span></button>'
        for c in CATS
    )
    nav = "\n".join(
        f'<li><a href="#{e(c["id"])}">{e(c["name"])}</a><span>{len(tools_in(c["id"]))}</span></li>'
        for c in CATS
    )
    body = "\n".join(sections)
    nl = chr(10)

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(TITLE)} - {len(TOOLS)} free tools and scripts for Microsoft Intune admins</title>
<meta name="description" content="A searchable directory of {len(TOOLS)} free, community-built Microsoft Intune tools: troubleshooting, app packaging, Autopilot, reporting, security baselines, macOS and Graph API automation.">
<link rel="canonical" href="{SITE}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Deep Shah">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(TITLE)}">
<meta property="og:title" content="{e(TITLE)} - {len(TOOLS)} free tools for Intune admins">
<meta property="og:description" content="Searchable directory of {len(TOOLS)} community-built Microsoft Intune tools across {len(CATS)} categories.">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{SITE}og-image.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(TITLE)} - {len(TOOLS)} free tools for Intune admins">
<meta name="twitter:description" content="Searchable directory of {len(TOOLS)} community-built Microsoft Intune tools.">
<meta name="twitter:image" content="{SITE}og-image.svg">
<meta name="theme-color" content="#101A2E">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
{json_ld()}
</head>
<body>
<a class="skip" href="#results">Skip to the tools</a>

<header class="top">
  <div class="wrap top-in">
    <p class="mark">Awesome Intune Tools</p>
    <nav class="top-links">
      <a href="{REPO}" rel="noopener">Source on GitHub</a>
      <a href="{REPO}#contributing" rel="noopener">Add a tool</a>
    </nav>
  </div>
</header>

<section class="hero">
  <div class="wrap">
    <h1>Find the right Intune tool without opening twelve tabs.</h1>
    <p class="lede">{len(TOOLS)} community-built tools, scripts and utilities for Microsoft Intune administrators, sorted into {len(CATS)} categories and checked for broken links. Start typing to narrow the list.</p>

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
    <p class="rail-note">Updated {TODAY}. Every link is verified by an automated check.</p>
  </aside>

  <main id="results">
{body}
    <p class="empty" id="empty" hidden>Nothing matches that. Try a shorter word, or <button type="button" id="reset">clear the filters</button>.</p>
  </main>
</div>

<footer class="foot">
  <div class="wrap">
    <p>Maintained by <a href="https://github.com/Deepshah0308" rel="noopener">Deep Shah</a>. The list is licensed <a href="http://creativecommons.org/licenses/by/4.0/" rel="noopener license">CC BY 4.0</a>; each tool is licensed by its own author.</p>
    <p>Missing something good? <a href="{REPO}#contributing" rel="noopener">Open a pull request</a>.</p>
  </div>
</footer>

<script src="app.js" defer></script>
</body>
</html>
"""
    (DOCS / "index.html").write_text(doc, encoding="utf-8")


def build_seo_files():
    urls = [SITE] + [f"{SITE}#{c['id']}" for c in CATS]
    body = "".join(
        f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod>"
        f"<changefreq>weekly</changefreq><priority>{'1.0' if i == 0 else '0.7'}</priority></url>"
        for i, u in enumerate(urls)
    )
    (DOCS / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + body + "</urlset>",
        encoding="utf-8",
    )
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "tools.json").write_text(json.dumps(DATA, indent=2), encoding="utf-8")


if __name__ == "__main__":
    build_readme()
    build_site()
    build_seo_files()
    print(f"Built {len(TOOLS)} tools in {len(CATS)} categories.")
