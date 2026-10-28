# Installation

The skill is plain Markdown. There is no package to install, no server to run and no API key to configure. The only optional dependency is Python for the repository validator and PDF tooling.

## Requirements

- An agent that can read Markdown instruction files and has access to web/search tools for live data.
- Optional: Python 3.9+ for `scripts/validate.py`.
- Optional: `tiktoken` for exact token counts (`pip install -r requirements-dev.txt`).
- Optional: Chromium and PyMuPDF for the PDF production workflow in `skill/references/pdf-report-production.md`.

If the agent has no web access, it can still use the method, but it must mark live-data lenses `not assessable` rather than invent numbers.

---

## Hermes Agent

### Windows (PowerShell)

```powershell
git clone https://github.com/Elfonius/professional-investor-analysis.git
New-Item -ItemType Directory -Force "$env:LOCALAPPDATA\hermes\skills\research\professional-investor-analysis" | Out-Null
Copy-Item -Recurse "professional-investor-analysis\skill\*" "$env:LOCALAPPDATA\hermes\skills\research\professional-investor-analysis\"
```

### macOS / Linux

```bash
git clone https://github.com/Elfonius/professional-investor-analysis.git
mkdir -p ~/.hermes/skills/research/professional-investor-analysis
cp -R professional-investor-analysis/skill/. ~/.hermes/skills/research/professional-investor-analysis/
```

Restart Hermes or reload skills. The skill is discovered as `professional-investor-analysis`.

If your Hermes profile uses a custom skills directory, copy the contents of `skill/` into `<profile>/skills/research/professional-investor-analysis/` instead. The important part is that `SKILL.md` sits at the root of the installed skill folder and `references/` and `templates/` are siblings.

### Verify

Ask the agent:

```text
List the skills you can see. Is professional-investor-analysis available?
```

Then run a smoke test:

```text
Use professional-investor-analysis to screen a fictional asset.
Show the investability gate, the scorecard and the limits. Do not invent data.
```

---

## Claude Code

Claude Code supports Agent Skills with a `SKILL.md` file. Project scope:

```bash
mkdir -p .claude/skills/professional-investor-analysis
cp -R professional-investor-analysis/skill/. .claude/skills/professional-investor-analysis/
```

User scope:

```bash
mkdir -p ~/.claude/skills/professional-investor-analysis
cp -R professional-investor-analysis/skill/. ~/.claude/skills/professional-investor-analysis/
```

If your Claude Code version uses a different skills path, check its documentation. The repository layout is already in the expected `SKILL.md` + supporting files form.

---

## Codex, Cursor and other agents

There is no universal skill standard. Use one of these patterns:

### A. Instruction file

Add a short pointer to `AGENTS.md` (Codex) or the project rules file:

```markdown
## Investment research

When the user asks for investment research, due diligence or a valuation, read
`skills/professional-investor-analysis/SKILL.md` first. Load files from
`references/` only when the matching lens is material. Use `templates/` for the
deliverable. Never invent data; mark missing evidence as "not assessable".
```

Keep the installed skill folder in the repository:

```text
skills/professional-investor-analysis/
├── SKILL.md
├── references/
└── templates/
```

Copy it from `skill/` in this repository. The agent reads `skills/professional-investor-analysis/SKILL.md`; the references and templates are siblings.

### B. System prompt

Paste the contents of `SKILL.md` into the agent's system prompt or custom instruction field. Keep `references/` and `templates/` in the workspace and tell the agent to read them on demand.

### C. Retrieval

Index `SKILL.md` and `references/*.md` in your retrieval system. Put `SKILL.md` in the always-on context and retrieve references by lens name. Do not retrieve all 11 references on every turn; that defeats the progressive-disclosure design.

### Generic loader prompt

```text
You have access to the Professional Investor Analysis skill at
./skills/professional-investor-analysis.

Before any investment analysis:
1. Read SKILL.md in full.
2. Identify the decision, horizon, numeraire, benchmark and constraints.
3. Build the evidence ledger before writing prose.
4. Load references/<topic>.md only for lenses that are material.
5. Use templates/investment-screen-en.md, investment-memo-en.md or
   investment-report-en.md for the deliverable.

Never invent a number, source or date. If a lens cannot be assessed, write
"not assessable" and name the missing input.
```

---

## Updating

```bash
cd professional-investor-analysis
git pull
cp -R skill/. ~/.hermes/skills/research/professional-investor-analysis/
```

Then reload skills or restart Hermes. If you customized templates, keep your changes in a separate branch or fork; do not overwrite them blindly.

## Uninstalling

Remove the skill folder from the agent's skills directory. Nothing else is installed.

## Troubleshooting

| Symptom | Check |
|---|---|
| Skill not listed | `SKILL.md` must be at the root of the skill folder; the folder name should match the `name` field. |
| Agent ignores references | The loader prompt must tell it to read `SKILL.md` first and load references by lens. |
| Token budget warning | The core is ~4,100 tokens. Do not paste all references into the system prompt. |
| Turkish characters break in PDF | Embed a Turkish-capable TTF; see `skill/references/pdf-report-production.md`. |
| Agent invents data | Add the "not assessable" rule to the system prompt and ask for an evidence ledger before prose. |
| Agent produces a score | Remove the request for a score; the method deliberately reports dimensions separately. |

## No credentials

This repository contains no API keys, tokens, cookies or personal account data. Do not add any. If you connect a data provider, keep credentials in your agent's secret store, never in the skill folder.
