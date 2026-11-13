# Open Questions and Proposed Decisions

The following items have not all been explicitly ratified as standard behavior. Do not treat proposals as authoritative without approval.

1. **Duplicate keys:** last-wins with a warning was proposed. Confirm whether this should be universal.
2. **Empty values:** distinguish bare flag, `KEY:`, and `KEY:''` in the formal conformance fixtures.
3. **Malformed quote recovery:** user requested termination at underscore or metadata end; precisely define how to handle a later quote in a subsequent argument.
4. **Literal underscores in positional fields:** quoted positional fields were proposed. Confirm interoperability with vendor CLI quoting.
5. **Value typing:** decide when plain numeric strings, leading-zero identifiers, booleans and signed numbers are converted versus preserved.
6. **Mixed lists and ranges:** decide whether duplicates are removed, and whether order is preserved.
7. **Unquoted `::` inside metadata values:** define valid usage and IPv6-bracket precedence.
8. **Limits:** define maximum accepted input length, range expansion limit and handling of extra positional fields.
9. **positional device function:** define whether fourth position is unrestricted text or a structured `DEVICE-FUNCTION-PORT-FUNCTION` pair.
10. **Whitespace:** confirm trimming outside quotes and preservation inside quotes.

## Operational safety
A forgiving parser may normalize syntax, but invalid service VLANs, addresses, unknown device commands or out-of-range settings must be caught before provisioning.
