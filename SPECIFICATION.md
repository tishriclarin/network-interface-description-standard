# NIDS Specification v1.0 (draft)

## Format

```text
LEGACY::KEY:VALUE_KEY:VALUE_FLAG
```

The first unquoted `::` starts metadata. Legacy-only descriptions are valid. Metadata-only descriptions start with `::`.

## Legacy positional fields

Full order: `SOURCE_DESTINATION_LAYER_DEVICE-FUNCTION_DESCRIPTION`.

- No legacy content: all positions null.
- One nonempty field: destination.
- Two fields: source, destination.
- Three or more: third is layer (L2 or L3 when provided), fourth is function, fifth is optional description.
- Empty fields between underscores omit that position without shifting following fields: `source_destination__router_description` gives layer=null and function=router.
- Layer is **never defaulted**.
- A quoted legacy field can contain an underscore.

## Metadata

- Underscore separates arguments, except inside correctly closed single-quoted strings.
- First colon in an argument separates key and value; a bare key is a true flag.
- Keys are case-normalized to uppercase; hyphens are allowed in keys.
- Values in single quotes are literal strings. Embedded apostrophe is written `''`.
- IPv6 addresses use brackets, e.g. `IP:[2001:db8::1]`.
- Unquoted commas separate list items; empty list items are discarded.
- Unquoted integer ranges such as `100-102` are inclusive; comma lists can mix ranges.
- Unclosed single quotes terminate at the next underscore or metadata end, with a warning.
- Duplicate keys use last value with a warning; empty arguments are ignored.
- Unknown keys are preserved. Parsed values must be validated for the target equipment before provisioning.

## Examples

```text
source_destination__router_description::VLAN:1,2,,3_DESC:'Customer''s Link'
::SERVICE-VLAN:151_CUSTOMER-VLAN:100_DHCP-OPTION82
CORE_EDGE_L3_ROUTER-UPLINK::IP:[2001:db8::1]
```

## Compatibility and safety

Descriptions have vendor-specific length and escaping limits. Do not treat parser acceptance as permission to execute commands. Always validate target-specific types and limits, and compare device read-back before declaring provisioning successful.
