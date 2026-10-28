# FAQ

### Is this investment advice?

No. It is a research method and a set of templates. It does not know your circumstances, cannot verify private information and does not guarantee a return. Nothing in this repository is a recommendation to buy or sell any asset.

### Does it work only for crypto?

No. Crypto is the primary track, but the method covers public equities, banks and insurers, credit, funds and ETFs, private companies, real assets, commodities and derivatives. The asset-class branch is in `skill/references/methodology-and-sources.md`.

### Does it require Hermes?

No. It is plain Markdown. Hermes users get the native skill loader and `skill-audit`; Claude Code, Codex, Cursor and other agents can load `skill/SKILL.md` as instructions and read the references on demand. See `docs/INSTALL.md`.

### Does it need API keys or a database?

No. The skill itself has no runtime. The agent needs web/search tools for live data. If it has no access, it must mark the affected lenses `not assessable` rather than invent numbers.

### Why is there no composite score?

A single score hides the trade-off that matters: a strong product can sit on a weak instrument, a cheap valuation can sit on an unenforceable right, and a good business can be a bad price. The skill reports the dimensions separately and makes the verdict conditional.

### Why does the gate say `insufficient evidence` instead of `conditional`?

`conditional` means a material component is weak but known; the condition can be written. `insufficient evidence` means a critical unknown prevents a judgment. Treating an unknown as a soft condition would launder missing evidence into a positive verdict.

### Can I use it for a private company with no public data?

Yes, but the output will be limited by the data room. The method separates the business, the cap table, the investment rights and the exit path. If documents are missing, the report must say which ones and how that limits the verdict.

### Why are some templates in Turkish?

The skill originated in a Turkish workflow. The English templates are the default for this repository; the Turkish ones are kept for parity. The method is language-independent.

### How do I customize it?

Edit the templates for house style; add a reference for a new asset class or lens; keep `skill/SKILL.md` stable unless you are changing the method. Run `python scripts/validate.py . --strict` after changes. See `docs/ARCHITECTURE.md`.

### How is quality measured?

Structural quality: `scripts/validate.py` and, in Hermes, `skill-audit`. Method quality: whether the evidence ledger, gate and counter-thesis are complete and whether a second reader can reproduce the conclusion. Neither proves predictive accuracy. A well-structured report can still be wrong.

### Can I use it commercially?

Yes, under the MIT license. Attribution is appreciated but not required beyond the license terms.

### How do I report a security issue?

Use GitHub Security Advisories, not a public issue. See `SECURITY.md`.

### Why does the repository include a real report about a token?

It is an example of the deep-report production standard: 14 pages, a one-page executive summary, charts, a scenario table, a risk matrix and a monitoring dashboard. The data is as of 2026-10-28 and is not a current recommendation. The fictional screen and IC memo show the reasoning without attaching it to a real asset.

### What is the difference between the screen, memo, report and workpaper?

The screen is a one-page triage; the memo is a 3–5 page working decision; the report is an 8–15 page committee document with a PDF; the workpaper is the evidence ledger behind all of them. The report is the argument; the workpaper is the proof.
