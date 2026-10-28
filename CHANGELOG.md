# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses semantic versioning.

## [0.4.0] — 2026-10-28

### Added

- 14-lens coverage matrix with a "covered or explicitly excluded" rule.
- Three delivery modes: screen (1 page), standard (3–5 pages), deep (8–15 page PDF + IC summary + workpaper).
- Crypto references: legal/security, market intelligence, on-chain flows, technical/market structure, unit economics, valuation.
- Cross-asset references: team/organization, portfolio fit, PDF production.
- English templates: screen, memo, deep report, IC summary; Turkish templates retained.
- Investment committee summary and full deep-report templates.
- One-page executive summary requirement for deep reports.
- Behavioral-bias check and positioning/consensus section.
- Repository validator, GitHub Actions workflow and contribution templates.

### Changed

- Gate vocabulary is rendered in the report language while the internal tokens remain `pass` / `conditional` / `fail` / `insufficient evidence`.
- Crypto is the primary track; other asset classes remain fully available.
- Short reports are no longer allowed to silently drop critical lenses; the incompressible minimum is explicit.

## [0.3.0] — 2026-10-28

### Added

- 16-step procedure and two-layer delivery: short report plus evidence workpaper.
- Crypto gate (Tier 1) and economics track (Tier 2).
- Turkish short-report contract: 550–650 words, 1–2 pages, one table maximum.
- `references/crypto-diligence.md` and `templates/investment-raporu-tr.md`.

## [0.2.0] — 2026-10-27

### Added

- Team and management review.
- Private-company checklist.
- Asset-class branches for SaaS, biotech, REITs, banks/insurers, consumer, credit, funds/ETFs, private companies, real estate, commodities and derivatives.
- Investability gate, reverse valuation, total-return decomposition, behavioral-bias check.
- Comparison with public agent skills and investment-diligence frameworks.

## [0.1.0] — 2026-10-27

### Added

- Initial skill: fundamental analysis, token economics, technical analysis, evidence discipline and report template.
