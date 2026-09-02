#!/usr/bin/env python3
"""Verify every tool URL in data/tools.json still resolves.

Run manually or via the weekly GitHub Actions job. Exits non-zero if any link
is dead so a broken entry cannot sit unnoticed in the list.
"""
import json
import pathlib
import ssl
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = json.loads((ROOT / "data" / "tools.json").read_text(encoding="utf-8"))["tools"]

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) awesome-intunetools-linkcheck"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def check(tool):
    req = urllib.request.Request(tool["url"], headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
            return tool, r.status, ""
    except Exception as exc:
        return tool, getattr(exc, "code", 0), str(exc)[:90]


def main():
    with ThreadPoolExecutor(max_workers=16) as pool:
        results = list(pool.map(check, TOOLS))

    # 403 usually means the host dislikes automated traffic, not a dead link.
    broken = [r for r in results if r[1] not in (200, 403)]

    print(f"Checked {len(results)} links. {len(results) - len(broken)} healthy.")
    for tool, status, err in broken:
        print(f"  BROKEN [{status or 'error'}] {tool['name']} -> {tool['url']} {err}")

    if broken:
        sys.exit(1)


if __name__ == "__main__":
    main()
