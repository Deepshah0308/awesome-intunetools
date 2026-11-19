#!/usr/bin/env python3
"""Validate tool entries a pull request adds to data/tools.json.

The issue-form path is checked by triage.py; this is the same validation for
the pull-request path, which otherwise merges unchecked. Entries are compared
against the base branch so only what the PR adds is checked.

Usage: pr_check.py <base-tools.json>
"""
import json
import pathlib
import re
import sys

from submission import DATA_PATH, validate


def norm(url):
    return re.sub(r"^https?://(www\.)?", "", (url or "").rstrip("/")).lower()


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: pr_check.py <base-tools.json>")

    base = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    head = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    base_urls = {norm(t["url"]) for t in base["tools"]}
    added = [t for t in head["tools"] if norm(t.get("url")) not in base_urls]

    if not added:
        print("No new tool entries in this pull request.")
        return

    print(f"Checking {len(added)} new entr{'y' if len(added) == 1 else 'ies'}.\n")
    failed = 0
    for entry in added:
        # validate against base: against head each new entry matches itself
        rep = validate(entry, base)
        verdict = "PASS" if rep.ok and not rep.warns else ("REVIEW" if rep.ok else "FAIL")
        print(f"--- {entry.get('name', '(unnamed)')} [{verdict}]")
        print(rep.markdown() or "(no findings)")
        print()
        if not rep.ok:
            failed += 1

    if failed:
        sys.exit(f"{failed} of {len(added)} new entries have blocking issues.")
    print("All new entries pass. Warnings above still need a human eye.")


if __name__ == "__main__":
    main()
