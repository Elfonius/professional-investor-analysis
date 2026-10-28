# Architecture

## Repository vs skill package

The repository contains more than the installable skill:

```text
professional-investor-analysis/
├── skill/                  # copy this into your agent's skills directory
├── docs/                   # human documentation
├── examples/               # fictional screens + a real deep-report PDF
├── scripts/validate.py     # repository validator
└── .github/                # CI and contribution templates
```

The `skill/` folder is the installable unit; repository tooling stays outside it so the package remains dependency-free.

## Progressive disclosure

The skill is split into three layers:

| Layer | File(s) | Loaded |
|---|---|---|
| **Core method** | `skill/SKILL.md` (~4,054 tokens) | Always, when the skill is active |
| **Lens references** | `skill/references/*.md` | Only when the matching lens is material |
| **Output templates** | `skill/templates/*.md` | Only when producing the deliverable |

This keeps the always-on context small while preserving depth. Pasting every reference into the system prompt defeats the design and wastes context.

## Skill file map

Inside `skill/`:

```text
SKILL.md
├── When to use
├── Deliverable modes
├── 14-lens coverage matrix
├── 16-step procedure
├── Gates and standards
├── Evidence rules
├── Report architecture
├── PDF production
└── Verification

references/
├── methodology-and-sources.md      # asset-class index, source map, data hierarchy
├── crypto-diligence.md             # Tier 1/2/3 crypto checklist
├── crypto-legal-security.md        # jurisdiction, classification, audit, keys, incidents
├── crypto-market-intelligence.md   # community, news, sentiment, catalysts
├── crypto-onchain-flows.md         # holders, staking, protocol buys, root sales
├── crypto-technical.md             # trend, volatility, depth, derivatives
├── crypto-unit-economics.md        # revenue quality, margins, stress tests
├── crypto-valuation.md             # business vs token value, scenarios, expected return
├── team-and-org.md                 # founders, funding, cap table, key-person
├── portfolio-fit.md                # suitability, correlation, liquidity, macro, ESG, bias
└── pdf-report-production.md        # HTML → Chromium → PyMuPDF production standard

templates/
├── investment-screen-en.md         # 1 page
├── investment-memo-en.md           # 3–5 pages
├── investment-report-en.md         # 8–15 pages
├── investment-committee-en.md      # 1 page
├── investment-analysis.md          # evidence workpaper
└── *-tr.md                         # Turkish equivalents
```

## Lens-to-reference map

| Lens | Primary reference |
|---|---|
| Decision and suitability | `skill/references/portfolio-fit.md`, `skill/SKILL.md` |
| Asset and instrument | `skill/references/methodology-and-sources.md` |
| Market and competition | `skill/references/methodology-and-sources.md` |
| Business and product | `skill/references/crypto-unit-economics.md`, `skill/references/team-and-org.md` |
| Demand and revenue quality | `skill/references/crypto-unit-economics.md` |
| Unit economics | `skill/references/crypto-unit-economics.md` |
| Team and organization | `skill/references/team-and-org.md` |
| Instrument and token economics | `skill/references/crypto-diligence.md`, `skill/references/crypto-valuation.md` |
| Ownership and on-chain flows | `skill/references/crypto-onchain-flows.md` |
| Technical and market structure | `skill/references/crypto-technical.md` |
| Community, news and catalysts | `skill/references/crypto-market-intelligence.md` |
| Legal, regulation and security | `skill/references/crypto-legal-security.md` |
| Valuation | `skill/references/crypto-valuation.md` |
| Risk and portfolio fit | `skill/references/portfolio-fit.md`, `skill/references/crypto-technical.md` |

## Token budget

| Component | Approx. tokens |
|---|---:|
| `skill/SKILL.md` | 4,054 |
| Longest reference (`skill/references/crypto-diligence.md`) | ~4,000 |
| Other references | 700–3,500 each |
| Templates | 500–1,200 each |

The core is under the 5,000-token ceiling used by the repository validator. The references are deliberately separate; an agent should load one or two, not all eleven.

## How an agent should load it

1. Read `skill/SKILL.md` in full.
2. Identify the decision, asset class and material lenses.
3. Build the evidence ledger before writing prose.
4. Load `skill/references/<topic>.md` only for material lenses.
5. Load the output template that matches the mode.
6. Run the validation/checklist before delivery.

A generic loader prompt is in `docs/INSTALL.md`.

## Validation

`scripts/validate.py` checks:

- frontmatter presence and required fields;
- name format and length;
- description length and trigger;
- body line and token limits (tiktoken optional);
- reference and template pointers;
- placeholder leakage in `skill/SKILL.md` and `skill/references/`;
- table pipe consistency;
- relative links in the repository documents;
- required sections and procedure/lens counts.

Run the repository validator:

```bash
python scripts/validate.py . --strict
```

The GitHub Actions workflow runs the same command on every push and pull request.

## Adding a lens

1. Add a row to the 14-lens table in `skill/SKILL.md`.
2. Add a row to the workpaper matrix in `skill/templates/investment-analysis.md`.
3. Add a row to the scorecard in the screen, memo and report templates.
4. Add or extend a reference with the evidence standard.
5. Update the lens-to-reference map in this file.
6. Run `python scripts/validate.py . --strict` and review the package.

Do not add a lens only to the prose; if it is not in the matrix, it will be silently skipped.

## Adding an asset class

1. Add a branch to the asset-class table in `skill/references/methodology-and-sources.md`.
2. Add the valuation approach to `skill/references/crypto-valuation.md` or a new reference.
3. Add a section to the memo/report templates if the branch needs different fields.
4. Add a test/sample to `examples/`.
5. Update the README and this file.

## No runtime

There is no server, database, package or API client. The skill is Markdown plus an optional Python validator outside the skill package. This is intentional: it can run in any agent, be forked, diffed and reviewed like code.
