#!/usr/bin/env python3
"""Triage a tool-submission issue and write a report for the workflow to post.

Reads the issue body from ISSUE_BODY, writes a markdown comment to
triage-comment.md and a verdict (pass|review|fail) to triage-verdict.txt.
"""
import os
import pathlib

from submission import parse_issue, to_entry, validate

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    body = os.environ.get("ISSUE_BODY", "")
    fields = parse_issue(body)

    if not fields.get("name") and not fields.get("url"):
        comment = ("I could not read this as a tool submission. If you meant to suggest a tool, "
                   "please use the [submission form]"
                   "(https://deepshah0308.github.io/awesome-intunetools/submit.html) "
                   "so the details come through in a format I can check.")
        verdict = "fail"
    else:
        rep = validate(to_entry(fields))
        head = f"### Automated checks for **{fields.get('name') or 'this submission'}**\n"

        if rep.ok and not rep.warns:
            verdict = "pass"
            tail = ("\nEverything checks out automatically. A maintainer still reviews before it goes in.\n")
        elif rep.ok:
            verdict = "review"
            tail = ("\nNothing blocking, but the points above need a human eye before this goes in.\n")
        else:
            verdict = "fail"
            tail = ("\nThis cannot be added as-is. Fix the blocking items above and edit the issue \u2014 "
                    "the checks re-run automatically on every edit.\n")

        comment = (head + "\n" + rep.markdown() + "\n" + tail
                   + "\n<sub>Automated triage. These checks confirm the link is real and the "
                     "metadata is valid; they do not judge whether the tool is a good fit.</sub>")

    (ROOT / "triage-comment.md").write_text(comment, encoding="utf-8")
    (ROOT / "triage-verdict.txt").write_text(verdict, encoding="utf-8")
    print(f"verdict={verdict}")
    print(comment)


if __name__ == "__main__":
    main()
