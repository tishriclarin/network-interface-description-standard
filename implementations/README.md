# NIDS implementations

Reference implementations belong here. The core parser must remain independent of device CLI access and provisioning.

## Python
See [python/README.md](python/README.md) and [python/nids.py](python/nids.py).

Run tests from the repository root:

```sh
python3 -m unittest discover -s tests -v
```

## Rust (planned)
A Rust parser will be added after the shared JSON conformance fixtures are finalized. Both languages must produce equivalent results for the same input.

## Future vendor adapters
Keep device-specific validation and command generation separate from the core parser. Network changes require preview, validation and read-back verification.
