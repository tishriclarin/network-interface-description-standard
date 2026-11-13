"""NIDS reference parser: forgiving syntax, no device writes."""
from __future__ import annotations
import ipaddress
import re
from typing import Any

_RANGE = re.compile(r"^([0-9]+)-([0-9]+)$")
_KEY = re.compile(r"^[A-Za-z][A-Za-z0-9-]*$")


def _split_fields(text: str, *, recover_quotes: bool = False) -> tuple[list[str], list[str]]:
    fields, warnings, buf = [], [], []
    quoted = False
    bracket = 0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "'":
            if quoted and i + 1 < len(text) and text[i + 1] == "'":
                buf.extend(["'", "'"])
                i += 2
                continue
            quoted = not quoted
        elif ch == '[' and not quoted:
            bracket += 1
        elif ch == ']' and not quoted and bracket:
            bracket -= 1
        elif ch == '_' and bracket == 0:
            # Recovery: an unclosed quote ends at the next separator.
            if quoted and recover_quotes and "'" not in text[i + 1:]:
                quoted = False
                warnings.append('Recovered unclosed quote at underscore')
            if not quoted:
                fields.append(''.join(buf))
                buf = []
                i += 1
                continue
        buf.append(ch)
        i += 1
    if quoted:
        warnings.append('Recovered unclosed quote at end')
    fields.append(''.join(buf))
    return fields, warnings


def _decode(token: str, warnings: list[str]) -> Any:
    token = token.strip()
    if token.startswith("'"):
        if token.endswith("'") and len(token) >= 2:
            return token[1:-1].replace("''", "'")
        warnings.append('Unclosed quoted value')
        return token[1:].replace("''", "'")
    if token.startswith('[') and token.endswith(']'):
        inside = token[1:-1]
        try:
            return str(ipaddress.ip_interface(inside)) if '/' in inside else str(ipaddress.ip_address(inside))
        except ValueError:
            return token
    if ',' in token:
        out = []
        for item in token.split(','):
            item = item.strip()
            if not item:
                continue
            decoded = _decode(item, warnings)
            if isinstance(decoded, list):
                out.extend(decoded)
            else:
                out.append(decoded)
        return out
    match = _RANGE.fullmatch(token)
    if match:
        a, b = map(int, match.groups())
        if a <= b and b - a <= 4096:
            return list(range(a, b + 1))
        warnings.append('Range reversed or too large; preserved as text')
        return token
    if token.lower() == 'true':
        return True
    if token.lower() == 'false':
        return False
    if re.fullmatch(r'-?[0-9]+', token):
        return int(token)
    return token


def parse(description: str) -> dict[str, Any]:
    if not isinstance(description, str):
        raise TypeError('description must be a string')
    warnings: list[str] = []
    if '::' in description:
        positional_text, metadata_text = description.split('::', 1)
    else:
        positional_text, metadata_text = description, None
    positional = {'source': None, 'destination': None, 'layer': None, 'device_function': None, 'description': None}
    if positional_text:
        positions, notes = _split_fields(positional_text)
        warnings.extend(notes)
        positions = [p.strip().strip("'").replace("''", "'") or None for p in positions]
        if len(positions) == 1:
            positional['destination'] = positions[0]
        else:
            for name, value in zip(positional, positions):
                positional[name] = value
            if len(positions) > 5:
                warnings.append('Extra positional fields ignored')
            if positional['layer'] and positional['layer'].upper() not in ('L2', 'L3'):
                warnings.append('positional layer is not L2 or L3')
    metadata: dict[str, Any] = {}
    if metadata_text is not None:
        fields, notes = _split_fields(metadata_text, recover_quotes=True)
        warnings.extend(notes)
        for field in fields:
            field = field.strip()
            if not field:
                continue
            key, sep, value = field.partition(':')
            key = key.strip().upper()
            if not _KEY.fullmatch(key):
                warnings.append(f'Invalid key skipped: {key!r}')
                continue
            if key in metadata:
                warnings.append(f'Duplicate key {key}; last value wins')
            metadata[key] = _decode(value, warnings) if sep else True
    return {'legacy': positional, 'metadata': metadata, 'warnings': warnings}
