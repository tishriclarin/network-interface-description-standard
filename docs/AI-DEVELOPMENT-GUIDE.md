# AI Development Guide — NIDS

## Purpose
This document is the primary onboarding reference for AI coding assistants implementing or consuming the Network Interface Description Standard (NIDS). Read [SPECIFICATION.md](../SPECIFICATION.md) first, then [GRAMMAR.md](../GRAMMAR.md), then the reference Python implementation and tests.

## Non-negotiable agreed rules
- Format: `positional::KEY:VALUE_KEY:VALUE_FLAG`.
- positional fields: source, destination, layer, device function, description; a lone positional field is destination; explicit empty positions retain their slot.
- Missing layer remains null; never infer L2.
- `::` marks the transition to metadata; metadata-only descriptions are allowed.
- Metadata keys may contain hyphens; underscores separate arguments.
- Unquoted commas form lists; unquoted integer hyphens denote inclusive ranges. Quoted strings preserve commas and hyphens literally.
- Single quotes delimit literals; doubled apostrophes represent a literal apostrophe.
- IPv6 literals are bracketed.
- Parsing is tolerant of empty list members and incomplete quotes; incomplete quotes terminate at a separator or metadata end.
- Parsing and provisioning validation are distinct. Never execute device commands solely because parsing succeeded.

## AI implementation instructions
1. Preserve backward compatibility. Do not silently change the meaning of existing examples.
2. Build deterministic tokenization with quote and bracket state, not simple string splitting.
3. Return original text, normalized parsed values, and recoverable warnings.
4. Never invent values for omitted positions or missing provisioning fields.
5. Treat unknown metadata keys as data, not as executable commands.
6. Limit numeric range expansion; perform device-specific validation before changes.
7. Write regression tests for each bug and for each new syntax rule.
8. Keep vendor adapters separate from the core parser.
9. Prefer documented behavior over speculative interpretations. Mark unresolved questions as proposals.
10. Do not claim tests pass without executing them.

## Recommended consumer integration
- Parse description -> inspect warnings -> validate application-specific keys and limits -> construct preview -> optionally apply device changes -> read back and verify.
- Never use an LLM's interpretation as the sole basis for a configuration write.

## Relevant files
- `SPECIFICATION.md`: human-readable syntax and semantics
- `GRAMMAR.md`: informative grammar
- `COMPATIBILITY.md`: vendor integration considerations
- `implementations/python/nids.py`: initial reference implementation
- `tests/`: conformance and recovery examples
- `docs/ROADMAP.md`: implementation plan
- `docs/OPEN-QUESTIONS.md`: unresolved choices
