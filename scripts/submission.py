#!/usr/bin/env python3
"""Parse and validate a tool-submission issue.

Shared by the triage workflow (which reports) and the approve workflow (which
adds the entry). Kept in one module so an approval can never accept something
triage would have rejected.

Checks fall into two buckets:
  FAIL  - blocks the submission outright (dead link, duplicate, bad category)
  WARN  - worth a human look, but not disqualifying (archived repo, few stars)

No check here decides whether a tool is *good*. That stays with a maintainer.
"""
from __future__ import annotations

import difflib
import json
import os
import pathlib
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "tools.json"

UA = "awesome-intunetools-triage (+https://github.com/Deepshah0308/awesome-intunetools)"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

VALID_KINDS = {"repo", "web", "guide"}

# Phrases that suggest a parked domain or an empty placeholder page.
DEAD_PAGE_MARKERS = [
    "domain is for sale", "buy this domain", "domain for sale",
    "coming soon", "under construction", "parked domain",
    "this site can't be reached", "account suspended",
    "default web site page", "welcome to nginx",
]

# Signals that a submission is a commercial product rather than a community tool.
COMMERCIAL_MARKERS = [
    "start your free trial", "request a demo", "book a demo",
    "per user per month", "per device per month", "pricing plans",
    "contact sales", "enterprise pricing",
]


# ---------------------------------------------------------------- fetching
def fetch(url, timeout=30, max_bytes=400_000):
    """GET a URL. Returns (status, final_url, text, error)."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            body = r.read(max_bytes)
            charset = r.headers.get_content_charset() or "utf-8"
            return r.status, r.geturl(), body.decode(charset, errors="replace"), None
    except urllib.error.HTTPError as exc:
        return exc.code, url, "", f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - report anything that stops a reader
        return 0, url, "", str(exc)[:120]


def visible_text(html_text):
    t = re.sub(r"<(script|style|noscript).*?</\1>", " ", html_text, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def page_title(html_text):
    m = re.search(r"<title[^>]*>(.*?)</title>", html_text, re.S | re.I)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


# ---------------------------------------------------------------- parsing
def parse_issue(body):
    """Pull fields out of a GitHub issue-form body (### Heading / value)."""
    if not body:
        return {}
    blocks = re.split(r"^###\s+", body, flags=re.M)[1:]
    fields = {}
    for block in blocks:
        head, _, rest = block.partition("\n")
        fields[head.strip().lower()] = rest.strip()

    def pick(*names):
        for n in names:
            v = fields.get(n)
            if v and v.lower() not in ("_no response_", "none"):
                return v.strip()
        return ""

    return {
        "name": pick("tool name"),
        "url": pick("link", "url"),
        "author": pick("author or maintainer", "author"),
        "category": pick("category").lower(),
        "kind": pick("type", "kind").lower(),
        "desc": " ".join(pick("what problem does it solve?", "description").split()),
        "notes": pick("anything else?", "notes"),
    }


# ---------------------------------------------------------------- checks
class Report:
    def __init__(self):
        self.fails, self.warns, self.notes = [], [], []

    def fail(self, msg):
        self.fails.append(msg)

    def warn(self, msg):
        self.warns.append(msg)

    def note(self, msg):
        self.notes.append(msg)

    @property
    def ok(self):
        return not self.fails

    def markdown(self):
        lines = []
        if self.fails:
            lines.append("**Blocking issues**\n")
            lines += [f"- {m}" for m in self.fails]
            lines.append("")
        if self.warns:
            lines.append("**Worth a look**\n")
            lines += [f"- {m}" for m in self.warns]
            lines.append("")
        if self.notes:
            lines.append("**Checks passed**\n")
            lines += [f"- {m}" for m in self.notes]
            lines.append("")
        return "\n".join(lines).strip()


def check_github_repo(url, rep):
    """Inspect a GitHub repo via the API for signs of life."""
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)", url)
    if not m:
        return
    owner, repo = m.group(1), m.group(2).removesuffix(".git")

    api = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(api, headers={
        "User-Agent": UA, "Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
            info = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            rep.fail(f"No public repository at `{owner}/{repo}` \u2014 the link is dead or private.")
            return
        if exc.code in (401, 403):
            # Rate limited or blocked: fall back to fetching the HTML page so a
            # dead link still gets caught rather than silently passing.
            status, _, body, _ = fetch(url)
            if status == 404:
                rep.fail(f"No public repository at `{owner}/{repo}` \u2014 the link is dead or private.")
            elif status == 200 and len(visible_text(body)) > 250:
                rep.warn(f"GitHub API unavailable (HTTP {exc.code}), but the repo page loads. "
                         "Stars and activity were not checked.")
            else:
                rep.fail(f"Could not confirm `{owner}/{repo}` exists (API HTTP {exc.code}, "
                         f"page HTTP {status}).")
            return
        rep.warn(f"GitHub API returned HTTP {exc.code} for `{owner}/{repo}`.")
        return
    except Exception as exc:  # noqa: BLE001
        rep.warn(f"Could not read the GitHub API for `{owner}/{repo}` ({str(exc)[:60]}).")
        return

    stars = info.get("stargazers_count", 0)
    pushed = info.get("pushed_at")
    rep.note(f"GitHub repo resolves: **{stars}** stars, license "
             f"`{(info.get('license') or {}).get('spdx_id', 'none')}`.")

    if info.get("archived"):
        rep.warn("The repository is **archived** \u2014 it may no longer be maintained.")
    if info.get("fork"):
        rep.warn("This is a **fork**. Check whether the upstream repo is the better link.")
    if info.get("private"):
        rep.fail("The repository is private, so nobody following the link could use it.")
    if not info.get("description"):
        rep.warn("The repository has no description set.")
    if stars < 3:
        rep.warn(f"Only {stars} stars. Not disqualifying for a new project, but worth a manual look.")

    if pushed:
        try:
            age = (datetime.now(timezone.utc)
                   - datetime.fromisoformat(pushed.replace("Z", "+00:00"))).days
            if age > 730:
                rep.warn(f"No commits in about {age // 365} years (last push {pushed[:10]}).")
            else:
                rep.note(f"Last pushed {pushed[:10]}.")
        except ValueError:
            pass


def check_live_page(url, rep):
    """Confirm a hosted tool or guide is a real page rather than a placeholder."""
    status, final, body, err = fetch(url)

    if status == 0:
        rep.fail(f"The link could not be fetched: {err}")
        return
    if status == 404 or status >= 500:
        rep.fail(f"The link returned HTTP {status}.")
        return
    if status == 403:
        rep.warn("The site returned HTTP 403 to an automated request. "
                 "That is often bot protection rather than a dead link \u2014 check by hand.")
        return
    if status != 200:
        rep.warn(f"The link returned HTTP {status}.")

    if final.rstrip("/") != url.rstrip("/"):
        rep.warn(f"Redirects to `{final}` \u2014 consider listing that URL instead.")

    text = visible_text(body)
    title = page_title(body)
    low = text.lower()

    for marker in DEAD_PAGE_MARKERS:
        if marker in low[:2000]:
            rep.fail(f"The page looks like a placeholder or parked domain "
                     f"(matched \u201c{marker}\u201d).")
            return

    if len(text) < 250:
        rep.fail(f"The page has almost no readable content ({len(text)} characters). "
                 "That usually means a placeholder, or a page that needs JavaScript to render.")
        return

    hits = [m for m in COMMERCIAL_MARKERS if m in low]
    if hits:
        rep.warn("Reads like a commercial product page (matched "
                 + ", ".join(f"\u201c{h}\u201d" for h in hits[:3])
                 + "). This list is for free and community tools.")

    rep.note(f"Page is live and has real content ({len(text):,} characters)."
             + (f" Title: \u201c{title[:90]}\u201d." if title else ""))


def validate(entry, data=None):
    """Run every check. Returns a Report."""
    rep = Report()
    data = data or json.loads(DATA_PATH.read_text(encoding="utf-8"))
    cat_ids = {c["id"] for c in data["categories"]}
    tools = data["tools"]

    # --- required fields
    for field, label in [("name", "Tool name"), ("url", "Link"),
                         ("author", "Author"), ("desc", "Description")]:
        if not entry.get(field):
            rep.fail(f"{label} is missing.")

    if not entry.get("url"):
        return rep

    url = entry["url"]
    if not url.startswith(("http://", "https://")):
        rep.fail("The link must start with `http://` or `https://`.")
        return rep
    if url.startswith("http://"):
        rep.warn("The link uses plain HTTP. Prefer HTTPS if the site supports it.")

    # --- taxonomy
    if entry.get("category") not in cat_ids:
        rep.fail(f"Category `{entry.get('category')}` is not one of: "
                 + ", ".join(sorted(cat_ids)) + ".")
    if entry.get("kind") not in VALID_KINDS:
        rep.fail(f"Type `{entry.get('kind')}` must be one of: repo, web, guide.")

    # --- description quality
    desc = entry.get("desc", "")
    if desc:
        if len(desc) < 40:
            rep.warn(f"The description is very short ({len(desc)} characters).")
        if len(desc) > 320:
            rep.warn(f"The description is long ({len(desc)} characters) and will be trimmed to house style.")

    # --- duplicates
    def norm(u):
        return re.sub(r"^https?://(www\.)?", "", u.rstrip("/")).lower()

    for t in tools:
        if norm(t["url"]) == norm(url):
            rep.fail(f"Already listed as **{t['name']}** ({t['url']}).")
            return rep

    if entry.get("name"):
        names = [t["name"] for t in tools]
        close = difflib.get_close_matches(entry["name"], names, n=1, cutoff=0.85)
        if close:
            rep.warn(f"Name is very similar to an existing entry, **{close[0]}**. "
                     "Check they are not the same project.")

    # --- is it real?
    if re.match(r"https?://(www\.)?github\.com/[^/]+/[^/#?]+", url):
        check_github_repo(url, rep)
    else:
        check_live_page(url, rep)

    return rep


def to_entry(fields):
    return {
        "name": fields["name"],
        "author": fields["author"],
        "url": fields["url"],
        "category": fields["category"],
        "kind": fields["kind"],
        "desc": fields["desc"],
    }
