#!/usr/bin/env python3
"""Verify every tool URL in data/tools.json still resolves.

Run manually or via the weekly GitHub Actions job. Exits non-zero if any link
is genuinely dead so a broken entry cannot sit unnoticed in the list.

Some hosts sit behind bot protection or rate limiting and will drop connections
when hit by a burst of parallel requests, even though the page is perfectly
reachable in a browser. To avoid failing the build on those, this script:

  * uses modest concurrency and a browser-like User-Agent,
  * retries anything that looks broken, serially and with backoff,
  * treats "I don't like robots" responses (403/405/429/999) as reachable.

Only URLs that still fail every retry are reported as broken.
"""
import json
import pathlib
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = json.loads((ROOT / "data" / "tools.json").read_text(encoding="utf-8"))["tools"]

# A plain scripted User-Agent gets blocked or tarpitted by several hosts.
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

# Codes that mean "the server is there and answering", even if it refuses us.
REACHABLE = {200, 201, 202, 203, 204, 206, 301, 302, 303, 307, 308,
             401, 403, 405, 429, 999}

WORKERS = 6          # low enough that no single host sees a burst
RETRIES = 3          # serial retries before calling a link dead
TIMEOUT = 45


def probe(url):
    """Single attempt. Returns (status_code, error_text)."""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close",
    })
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=CTX) as r:
            return r.status, ""
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except Exception as exc:  # noqa: BLE001 - report anything that stops a reader
        return 0, str(exc)[:90]


def check(tool):
    status, err = probe(tool["url"])
    return tool, status, err


def main():
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(check, TOOLS))

    suspect = [r for r in results if r[1] not in REACHABLE]

    # Retry serially with backoff. A host that rate-limited the parallel pass
    # will almost always answer on a calm second look.
    confirmed = []
    if suspect:
        print(f"{len(suspect)} link(s) failed the parallel pass; retrying serially...\n")
        for tool, status, err in suspect:
            for attempt in range(RETRIES):
                time.sleep(2 * (attempt + 1))
                status, err = probe(tool["url"])
                if status in REACHABLE:
                    print(f"  recovered on retry {attempt + 1}: {tool['name']}")
                    break
            else:
                confirmed.append((tool, status, err))

    healthy = len(results) - len(confirmed)
    print(f"\nChecked {len(results)} links. {healthy} healthy.")

    for tool, status, err in confirmed:
        label = status if status else "connection error"
        print(f"  BROKEN [{label}] {tool['name']} -> {tool['url']} {err}")

    if confirmed:
        sys.exit(1)


if __name__ == "__main__":
    main()
