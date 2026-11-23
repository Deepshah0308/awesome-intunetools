#!/usr/bin/env python3
"""Guards the two behaviours that would otherwise break quietly.

1. The site is a pure function of the repo. Rebuild it, or build it on a
   different day, and the bytes are the same. If this regresses, the weekly
   link check commits a diff every Monday whether or not anything moved.
2. A dead link still writes a report, still fails the job, and makes the
   site say "checked" rather than "verified".

Run: python scripts/selftest.py
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ["docs/index.html", "docs/sitemap.xml", "docs/submit.html",
       "docs/sponsor.html", "README.md"]
FAILED = []

# Build under a date far in the future without touching the real clock.
CLOCK = """import datetime as _d
class _D(_d.date):
    @classmethod
    def today(cls): return cls(2031, 7, 4)
_d.date = _D
import runpy; runpy.run_path('scripts/build.py', run_name='__main__')
"""

# Run the link checker against stubbed responses, so the test needs no network.
STUB = """import sys
sys.path.insert(0, 'scripts')
import linkcheck
linkcheck.probe = lambda url: (200, '') if 'good' in url else (0, 'stubbed failure')
linkcheck.RETRIES = 1
linkcheck.time.sleep = lambda *_: None
try:
    linkcheck.main()
except SystemExit as exc:
    sys.exit(exc.code or 0)
"""


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + (f"  ({detail})" if detail and not ok else ""))
    if not ok:
        FAILED.append(name)


def clone(dst):
    shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns(".git"))
    return pathlib.Path(dst)


def run(cwd, script):
    return subprocess.run([sys.executable, script], cwd=cwd, capture_output=True, text=True)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)

        a = clone(tmp / "repro")
        assert run(a, "scripts/build.py").returncode == 0
        first = {p: (a / p).read_bytes() for p in OUT}
        assert run(a, "scripts/build.py").returncode == 0
        check("rebuilding produces the same bytes",
              all((a / p).read_bytes() == first[p] for p in OUT))

        (a / "scripts/_clock.py").write_text(CLOCK, encoding="utf-8")
        assert run(a, "scripts/_clock.py").returncode == 0
        check("the system clock does not reach the output",
              all((a / p).read_bytes() == first[p] for p in OUT))

        b = clone(tmp / "deadlink")
        data = json.loads((b / "data" / "tools.json").read_text(encoding="utf-8"))
        cat = data["categories"][0]["id"]
        data["tools"] = [
            {"name": "Good", "author": "a", "url": "https://good.example/",
             "category": cat, "kind": "repo", "desc": "x"},
            {"name": "Dead", "author": "a", "url": "https://dead.example/",
             "category": cat, "kind": "repo", "desc": "x"},
        ]
        (b / "data" / "tools.json").write_text(json.dumps(data, indent=2) + "\n",
                                               encoding="utf-8")
        (b / "data" / "linkcheck.json").unlink(missing_ok=True)

        (b / "scripts/_stub.py").write_text(STUB, encoding="utf-8")
        result = run(b, "scripts/_stub.py")
        check("a dead link fails the job", result.returncode == 1,
              f"exit {result.returncode}")

        report = b / "data" / "linkcheck.json"
        check("a dead link still writes the report", report.exists())
        if report.exists():
            got = json.loads(report.read_text(encoding="utf-8"))
            check("the report names the dead link",
                  got.get("broken") == ["https://dead.example/"], str(got))

        assert run(b, "scripts/build.py").returncode == 0
        html = (b / "docs" / "index.html").read_text(encoding="utf-8")
        check('the site says "checked", not "verified", while a link is dead',
              "1/2 links checked" in html and "links verified" not in html)

    if FAILED:
        print(f"\n{len(FAILED)} check(s) failed.")
        sys.exit(1)
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
