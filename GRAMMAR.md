# NIDS Grammar (informative)

```text
description = positional [ '::' metadata ] | '::' metadata
metadata    = argument *( '_' argument )
argument    = key [ ':' value ]
key         = letter *( letter | digit | '-' )
value       = quoted | unquoted
quoted      = "'" *( ordinary-char | "''" ) "'"
```

This is an informative grammar, not a strict parser specification: recovery from unclosed quotes, duplicate keys, and empty list elements is defined in SPECIFICATION.md. A parser must track quote and IPv6 bracket state rather than blindly splitting delimiters.
