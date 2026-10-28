# Usage

## Choose the mode first

| Mode | Ask for it when | Output |
|---|---|---|
| **Screen** | You need a first look, a comparison or a triage | 1 page, 300–500 words |
| **Standard** | You are making a working decision with moderate evidence | 3–5 page memo |
| **Deep** | You need a committee-ready report, a PDF, or "every perspective" | 8–15 page PDF + 1-page IC summary + workpaper |

If you do not specify, the skill chooses the smallest mode that fits the decision. A buy/size/hold/exit decision defaults to deep.

---

## Prompt recipes

### Screen

```text
Use professional-investor-analysis in screen mode.

Asset: <name / ticker / contract>
Decision: is this worth a deeper look?
Horizon: 12 months
Numeraire: USD

Start with the investability gate. Then give me the product case, the instrument
case, valuation range, the three critical risks and a conditional verdict.
Mark every lens you cannot assess as "not assessable" and name the missing input.
```

### Standard memo

```text
Use professional-investor-analysis in standard mode.

Asset: <name>
Decision: buy / hold / exit
Horizon: 24 months
Numeraire: USD
Constraints: <tolerable drawdown, liquidity needs, jurisdiction; or "none supplied">

Produce a 3–5 page memo with an evidence ledger, a scorecard, a valuation range,
a counter-thesis and a monitoring dashboard. No composite score.
```

### Deep report / PDF

```text
Use professional-investor-analysis in deep mode.

Asset: <name>
Decision: investment committee review
Horizon: 12 months
Numeraire: USD

Produce:
1. an 8–15 page A4 PDF with a cover, one-page executive summary, 13 sections,
   charts with source/date captions and page numbers;
2. a one-page investment committee summary;
3. the evidence workpaper.

Every number needs a source and an as-of date. Separate project quality,
instrument quality, price, timing and suitability. End with the conditions that
would reverse the verdict.
```

### Compare two assets

```text
Use professional-investor-analysis to compare <A> and <B>.

Decision: which one deserves the next diligence dollar, not which one will go up.
Use the same horizon, numeraire and evidence standard for both.
Show where the data is not comparable; do not force a ranking if the evidence
does not support one.
```

### Exit / hold review

```text
Use professional-investor-analysis to review an existing position in <asset>.

Do not ask whether I should have bought it. Ask whether the forward risk/reward
justifies holding it today. Check anchoring and sunk-cost bias. Do not infer my
position size. Give me the conditions that would make exiting rational.
```

### Crypto deep dive

```text
Use professional-investor-analysis in deep mode for <token / protocol / subnet>.

Start with the token and chain identity, supply reality, privileged control,
demand chain and legal eligibility. Then cover holder concentration, staking and
validator flows, emissions/unlocks, value capture, technical market structure,
community/news catalysts, valuation and exit liquidity.
```

### Equity / credit / private company

```text
Use professional-investor-analysis for <company>.

Asset class: <public equity | credit | private company | fund | real asset>
Decision: <...>
Horizon: <...>

Use the asset-class branch in skill/references/methodology-and-sources.md. For a private
company, separate the business from the cap table, the investment rights and the
exit path. For credit, cover covenants, recovery, rating trajectory and duration.
```

---

## Language and format

- Write in the user's language. The method is language-independent; English and Turkish templates are included.
- Keep tickers, contract addresses, fund names and function names verbatim.
- Use one date format consistently; state the timezone (UTC is the default).
- Use one number format consistently; state the currency and unit.
- Do not use a table unless it makes a comparison easier. The screen allows one table; the memo allows two or three.
- Do not deliver internal checklists, empty rows or `{{placeholders}}`.

## Evidence expectations

The agent should be able to show:

- the claim;
- the evidence type (fact, issuer claim, estimate, inference);
- the value, unit and date;
- the source and its independence;
- the status (verified, conflicting, unresolved, not assessable).

If it cannot, the correct output is `not assessable`, not a confident paragraph.

## PDF production

Deep mode uses the HTML → Chromium → PyMuPDF pipeline in `skill/references/pdf-report-production.md`. The repository does not bundle Chromium or PyMuPDF. Install them in the agent environment if you want PDF output; otherwise ask for Markdown and convert it with your own toolchain.

Minimum PDF standard:

- A4, 9.5–11 pt body, sans-serif headings;
- a cover and a one-page executive summary;
- 1–2 charts per major section, each with a source/date caption;
- page numbers and a footer;
- no internal checklist or empty table in the delivered file.

## Common mistakes

| Mistake | Fix |
|---|---|
| Asking for a single score | Ask for the dimensions and a conditional verdict. |
| Not supplying constraints | The skill will write "suitability not assessable"; that is correct. |
| Asking for a deep report with no data access | The skill will mark live lenses unassessable; provide sources or tools. |
| Pasting all references into the prompt | Load `skill/SKILL.md` always; load references by lens only. |
| Treating a bullish chart as evidence of value | Technicals are timing/context, not proof of the business case. |
| Copying a sample's numbers | Samples are fictional; use them for structure, not facts. |
