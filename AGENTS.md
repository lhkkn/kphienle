# portfolio — Agent Guide

> Project-specific rules. Supplements `~/Workspace/AGENTS.md`; where they disagree,
> this file wins for this project.

## What this is
kphienle.com — a public single-page personal portfolio. One static `index.html`
and a `CNAME`. Served by `python3 http.server` on `127.0.0.1:8781`
(`kphienle.service`) behind the Cloudflare tunnel `kphienle`. There is no build
step, so this project is notes-only in the build sense: nothing compiles.

## Verification model

Standard: ~/Workspace/work/notes/VERIFICATION.md. A test is a claim cheaper to check than to trust — verify at the assertion, not the directory.

- **Gate:** `make check` — `check.py` confirms `index.html` is a complete HTML document and `CNAME` is a single domain (tier 0). Deterministic, offline.
- **Eval:** none.
- **Tiers in use:** 0 static.
- **Rules:** stub only the boundary; never mock the subject; remove mirrors.
- **Regression seeds:** none yet.
