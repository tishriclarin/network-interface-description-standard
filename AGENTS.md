# Instructions for AI coding agents

This repository defines NIDS, a vendor-neutral network interface description format. Before modifying code, read `SPECIFICATION.md`, `GRAMMAR.md`, and `docs/AI-DEVELOPMENT-GUIDE.md`.

## Development rules
- Do not change agreed syntax or positional positional semantics without an explicit specification update.
- Missing L2/L3 must remain null.
- Preserve omitted positional fields and tolerate recoverable user input mistakes.
- Never turn parser warnings into silent network configuration changes.
- Keep parsing independent from network connections, device CLI, or vendor-specific provisioning.
- For behavior changes, update the specification and add regression tests.
- Run `python3 -m unittest discover -s tests -v` before claiming Python conformance.
- Document known limitations and outstanding decisions rather than guessing.
