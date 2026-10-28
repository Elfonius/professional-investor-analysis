# Contributing

Thanks for improving the skill. The goal is not more prose; it is a more auditable method.

## Before you open a PR

1. Read `skill/SKILL.md`, `docs/METHODOLOGY.md` and the reference you are changing.
2. Check whether the change is a **method** change or a **template** change.
   - Method: `skill/SKILL.md`, `skill/references/`.
   - Output: `skill/templates/`, `examples/`.
3. Add or update an example if the change affects the output shape.
4. Run:

```bash
python scripts/validate.py . --strict
```

5. If you use Hermes, run the skill audit and include the result in the PR.

## Evidence standard

Investment content is held to a higher bar than ordinary documentation.

- Every factual claim needs a source, a date and a definition of the metric.
- An issuer claim is not a fact. Label it as a claim and say what would verify it.
- Do not add a hard-coded threshold ("slippage must be 2%") unless it is a documented standard. Prefer a measurement and a disclosure rule.
- Do not add a price target, a guaranteed return or a composite score.
- Do not use promotional language ("risk-free", "guaranteed", "audited" without the audit scope).
- If you cannot verify a claim, write `not assessable` or remove it.

## What makes a good change

- A new lens or asset class with a clear evidence standard and a template row.
- A sharper gate component that prevents a known failure mode.
- A template that makes the output easier to review without hiding uncertainty.
- A validator check that catches a real class of defect.
- A documentation fix that removes ambiguity.

## What to avoid

- Adding length without adding a decision rule.
- Adding a fixed score or ranking that hides trade-offs.
- Adding a vendor-specific dependency to the core skill.
- Copying a commercial report or a paywalled source without permission.
- Personal data, client names, API keys or local paths.

## Commit style

Use a clear, imperative subject:

```text
Add credit covenant checklist
Fix broken valuation reference
Clarify gate vocabulary
```

## Pull request checklist

- [ ] The change is scoped to one idea.
- [ ] `python scripts/validate.py . --strict` passes.
- [ ] New pointers resolve on disk.
- [ ] No personal data, credentials or local absolute paths.
- [ ] No hard-coded score, price target or guarantee.
- [ ] If the method changed, `docs/METHODOLOGY.md` and the lens matrix were updated.
- [ ] If the output changed, a template or example was updated.
- [ ] The PR description explains the failure mode the change prevents.

## Review standard

A reviewer should be able to answer:

1. What decision does this change improve?
2. What evidence standard does it enforce?
3. What does it make harder to fake?
4. Does it add a new way to hide uncertainty?

If the answer to (4) is yes, the change needs a redesign.

## License

By contributing, you agree that your contribution is licensed under the MIT license in `LICENSE`.
