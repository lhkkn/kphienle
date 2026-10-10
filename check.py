#!/usr/bin/env python3
"""Static gate for a single-page site. Offline, deterministic.

Checks that index.html exists and is a complete HTML document, and (if present)
that CNAME is a single non-empty domain. No network.
"""
from __future__ import annotations

import pathlib
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent
INDEX = ROOT / "index.html"
REQUIRED = ("<!doctype html>", "<html", "</html>", "<head", "</head>", "<body", "</body>", "<title")


def main() -> int:
    rc = 0
    if not INDEX.exists() or not INDEX.read_text(encoding="utf-8", errors="replace").strip():
        print(f"FAIL: {INDEX.name} is missing or empty")
        return 1
    text = INDEX.read_text(encoding="utf-8", errors="replace")
    missing = [t for t in REQUIRED if t not in text.lower()]
    if missing:
        print(f"FAIL: {INDEX.name} is missing tags: {', '.join(missing)}")
        rc = 1
    try:
        HTMLParser().feed(text)
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL: {INDEX.name} did not parse: {exc}")
        rc = 1

    cname = ROOT / "CNAME"
    if cname.exists():
        host = cname.read_text(encoding="utf-8", errors="replace").strip()
        if not host or " " in host or "." not in host:
            print(f"FAIL: CNAME is not a single domain: {host!r}")
            rc = 1

    if rc == 0:
        print(f"ok: {INDEX.name} ({len(text)} bytes) is a complete HTML document")
    return rc


if __name__ == "__main__":
    sys.exit(main())
