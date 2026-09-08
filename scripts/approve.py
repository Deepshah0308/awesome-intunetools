#!/usr/bin/env python3
"""Add an approved submission to data/tools.json and rebuild the site.

Re-runs the full validation first, so an approval can never let through
something triage would have blocked.
"""
import json
import os
import pathlib
import subprocess
import sys

from submission import DATA_PATH, parse_issue, to_entry, validate

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    fields = parse_issue(os.environ.get("ISSUE_BODY", ""))
    entry = to_entry(fields)

    if not entry.get("url"):
        sys.exit("Could not parse a submission from this issue.")

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    rep = validate(entry, data)
    if not rep.ok:
        (ROOT / "approve-error.md").write_text(
            "Cannot add this automatically \u2014 the checks still fail:\n\n" + rep.markdown(),
            encoding="utf-8")
        sys.exit("Validation failed; refusing to add.")

    data["tools"].append(entry)
    DATA_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py")], check=True)

    (ROOT / "approve-result.md").write_text(
        f"Added **{entry['name']}** to "
        f"{[c['name'] for c in data['categories'] if c['id'] == entry['category']][0]}. "
        f"The list is now {len(data['tools'])} tools.\n\n"
        f"Live shortly at https://deepshah0308.github.io/awesome-intunetools/#{entry['category']}\n\n"
        "Links are re-checked automatically every week, so if the URL moves it will surface here.",
        encoding="utf-8")
    print(f"Added {entry['name']} ({len(data['tools'])} tools total)")


if __name__ == "__main__":
    main()
