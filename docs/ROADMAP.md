# NIDS Development Roadmap

## Phase 1 — Baseline specification (initial draft)
- [x] Establish repository, branding, specification and grammar documents
- [x] Record legacy positional semantics and metadata conventions
- [x] Add initial Python parser and example fixtures
- [ ] Review contradictions and ambiguous cases in the written specification
- [ ] Execute and pass all conformance tests

## Phase 2 — Harden the Python reference implementation
- [ ] Robust scanner for quoted legacy fields and metadata
- [ ] Recover unclosed quotes at the next underscore, even if later quotes exist
- [ ] Correct IPv6 lists, IPv6 endpoints, and bracket handling
- [ ] Preserve raw tokens, normalized tokens, warnings, and value types
- [ ] Test duplicate keys, missing values, ranges, whitespace and malformed input
- [ ] Publish versioned Python package, CLI and API documentation

## Phase 3 — Cross-language conformance
- [ ] Define language-neutral JSON fixtures with exact expected outputs
- [ ] Implement equivalent Rust parser
- [ ] Run Python and Rust implementations against the same fixtures
- [ ] Add GitHub Actions CI and release versioning

## Phase 4 — Vendor adapters
- [ ] Cisco Nexus / NX-OS examples and limits
- [ ] Juniper Junos examples and limits
- [ ] MikroTik RouterOS examples and limits
- [ ] ZTE GPON OLT examples and limits
- [ ] Huawei examples and limits
- [ ] Device read-back and description-length validation

## Phase 5 — Integration and governance
- [ ] Integrate with zte-cli in preview mode first
- [ ] Document safe provisioning validation and rollback boundaries
- [ ] Publish compatibility matrix, changelog, contribution guide and release policy

This is a plan, not a claim of completed functionality.
