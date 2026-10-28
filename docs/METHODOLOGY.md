# Methodology

The method is designed to make an investment analysis **auditable**, not to make it sound authoritative. It does not predict prices. It forces the analyst — human or agent — to state the decision, expose the evidence, separate the questions and name the conditions under which the conclusion is wrong.

## The 16-step workflow

| # | Step | What must be true before moving on |
|---|---|---|
| 1 | Frame the decision | The decision, horizon, numeraire, benchmark, jurisdiction and constraints are explicit or labelled as assumptions. |
| 2 | Map the asset and the claims | The issuer, instrument, rights and chain/contract are separated; promotional claims are written as testable questions. |
| 3 | Build the evidence ledger | Every material claim has a type, value, unit, date, source and status. |
| 4 | Check freshness and comparability | Dates, units, currencies, supply definitions and peer periods are aligned; missing data is not zero. |
| 5 | Business and product | Real usage, pricing, distribution, cost structure and moat are evidenced. |
| 6 | Market and competition | Bottom-up market size, 3–5 peers, share and competitive dynamics are assessed. |
| 7 | Demand and unit economics | Paid versus incentivized demand, concentration, retention and unit margins are separated. |
| 8 | Team and governance | Founders, critical roles, track record, funding, cap table and key-person risk are assessed. |
| 9 | Instrument and token economics | Rights ladder, supply bridge, float/FDV, emissions, unlocks and value capture are mapped. |
| 10 | Ownership and on-chain flows | Holder concentration, staking, protocol buys, root sales, treasury and validator/miner control are measured. |
| 11 | Technical and market structure | Trend, relative strength, volatility, drawdown, depth, slippage and derivatives are described as timing/context. |
| 12 | Community, news and catalysts | Social, GitHub, governance, news flow and catalyst calendar are checked for evidence, not sentiment alone. |
| 13 | Legal, regulation and security | Jurisdiction, classification, KYC/AML, audit, key control and incidents are assessed. |
| 14 | Valuation | The method fits the asset; assumptions and sensitivities are visible; the current price is reverse-engineered. |
| 15 | Stress test and red-team | The strongest counter-thesis, tail scenarios and falsifiers are written. |
| 16 | Decide, monitor and deliver | The gate, verdict, conditions, monitoring dashboard and report are complete. |

The full lens table is in `skill/SKILL.md` and the repository README. Every lens must be covered or explicitly excluded as `not material` / `not assessable` with a reason.

## The investability gate

The gate is **non-compensatory**. It answers a narrower question than valuation:

> Can this asset be owned, verified, exited and legally held at all?

| Status | Meaning |
|---|---|
| `pass` | The critical components are evidenced; proceed to valuation. |
| `conditional` | A material component is weak or unresolved; the verdict must state the condition. |
| `fail` | A critical component is broken; a growth story, score or chart cannot offset it. |
| `insufficient evidence` | A critical unknown prevents a judgment. This is not the same as `conditional`. |

Typical gate components:

- **Asset and ownership:** what is the instrument, who issues it, what rights does it carry?
- **Claim chain:** can the critical claims be verified, and at what commit/version?
- **Custody and control:** who can move funds or upgrade the contract?
- **Exit:** is there a venue, depth and legal path to sell?
- **Eligibility:** can the intended investor legally hold it in their jurisdiction?

## Evidence classes

| Class | Example | How to use it |
|---|---|---|
| **Verified fact** | On-chain supply at a block; audited financial statement | Can support a conclusion; still record the date and method. |
| **Issuer claim** | "50 billion tokens per day"; "audited" | A claim to test; never repeat it as a fact without evidence. |
| **Estimate** | Bottom-up market size; normalized revenue | Label the assumptions and the range. |
| **Inference** | "This implies 30% paid demand" | Show the arithmetic and the inputs. |
| **Unresolved** | No public cap table; no audit scope | Write `not assessable`; do not fill the gap with a guess. |

## Asset-class branches

The core method is the same; the evidence and valuation branch changes.

| Asset class | Branch |
|---|---|
| Crypto token / protocol / subnet | `skill/references/crypto-diligence.md` + the six crypto references |
| Public operating company | Business/segment economics, cash conversion, debt/leases, consensus and short interest as positioning, sector multiples and cash-flow valuation |
| Bank / insurer | Regulatory capital, asset/credit quality, funding/liquidity, rate sensitivity, reserves/combined ratio, solvency |
| Credit | Yield/spread/recovery, rating trajectory, covenants, duration, default scenarios |
| Fund / ETF | NAV, fees, track record, liquidity, mandate and style drift |
| Private company | Data room, cap table, investment rights, dilution, governance, exit waterfall |
| Real estate / real asset | NOI, cap rate, occupancy, lease profile, capex, financing and exit |
| Commodity | Cost curve, inventory, marginal producer, transport, policy and cycle |
| Option / derivative | Payoff, Greeks, implied volatility, skew, collateral and path dependency |

The asset-class table in `skill/references/methodology-and-sources.md` gives the full checklist.

## Deliverable modes

| Mode | Standard |
|---|---|
| Screen | 1 page, 300–500 words, one table maximum, gate and verdict visible |
| Standard | 3–5 pages, evidence-led, 2–3 tables, counter-thesis and monitoring |
| Deep | 8–15 page A4 PDF, one-page executive summary, charts with source/date captions, IC summary, workpaper |

The mode changes the amount of evidence shown, not the standard of proof. A screen that skipped a Tier 1 control must say so.

## What "professional" means here

It means:

- the question is framed before the answer;
- the evidence is dated and sourced;
- the instrument is separated from the business;
- the valuation is method-appropriate and assumption-visible;
- the counter-thesis is as strong as the thesis;
- the verdict is conditional and falsifiable;
- the limits are stated.

It does **not** mean a licence, a guarantee, a price target or a composite score.

## Quality control

- `scripts/validate.py` checks the repository structure, links and token budget.
- The templates enforce the output contract.
- A second reader — human or agent — should be able to reproduce the evidence ledger and the gate from the report.

## Limitations

The method cannot create data that does not exist. It cannot verify private documents it cannot access. It cannot make a valuation correct. It can make the reasoning inspectable, the assumptions explicit and the conclusion honest about its limits.
