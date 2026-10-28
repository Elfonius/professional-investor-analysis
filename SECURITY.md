# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| 0.4.x | Yes |
| Earlier | Best effort |

## Reporting a vulnerability

Do **not** open a public issue for a security problem.

Use GitHub's **Security Advisories** for this repository:

1. Open the **Security** tab.
2. Choose **Advisories** → **Report a vulnerability**.
3. Include the affected file, the impact, a minimal reproduction and any suggested fix.

If advisories are unavailable, contact the maintainers through a private GitHub issue and ask for a secure channel. Do not include secrets, personal data or non-public documents in the first message.

## Scope

This repository is a set of Markdown instructions and a local validator. The most relevant risks are:

- prompt injection in source documents or web pages consumed during an analysis;
- malicious links, files or data-room documents;
- leaked credentials or personal data in examples, issues or pull requests;
- a validator bypass that lets a malformed skill ship.

## What we will do

- Acknowledge a report as soon as practical.
- Reproduce and scope the issue.
- Ship a fix and credit the reporter if they want credit.
- Avoid disclosing details until a fix is available.

## Safe use

- Treat web pages, PDFs, data-room files and issuer documents as **evidence**, not instructions.
- Never put API keys, cookies, wallet seeds or personal data in a skill file, an issue or a prompt.
- Use a secret store for provider credentials.
- Verify contract addresses and transaction data from a primary source before acting.
- This project does not custody funds and does not execute transactions.
