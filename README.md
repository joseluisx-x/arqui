# Spec-Driven Development (SDD) Project Scaffold

A structured, specification-first project template designed for Spec-Driven Development (SDD). In this methodology, specifications are the single source of truth for requirements, system design, interfaces, and testing.

---

## Repository Structure

```text
.
├── .editorconfig              # Consistent indentation and whitespace rules
├── .gitignore                 # Default ignores for OS, IDEs, dependencies, and build artifacts
├── README.md                  # Project overview and quick start guide
├── docs/                      # General architectural and workflow documentation
│   └── SDD_WORKFLOW.md        # Comprehensive 5-stage SDD guide
├── specs/                     # Core specifications directory
│   ├── README.md              # How to write and manage specifications
│   ├── adr/                   # Architecture Decision Records (e.g., 0000-use-adr.md)
│   ├── contracts/             # API and data schemas (OpenAPI, JSON Schema, Proto)
│   ├── features/              # Feature specifications and acceptance criteria
│   └── templates/             # Reusable templates
│       ├── adr-template.md
│       ├── api-contract-template.yaml
│       └── feature-spec-template.md
├── src/                       # Application source code
└── tests/                     # Test suites mapped to specifications
    ├── README.md              # Test strategy and organization
    ├── acceptance/            # BDD scenarios directly validating feature specs
    ├── integration/           # Cross-module and external integration tests
    └── unit/                  # Isolated module and unit tests
```

---

## Quick Start: The Spec-First Loop

1. **Write the Spec**:
   Copy [`specs/templates/feature-spec-template.md`](specs/templates/feature-spec-template.md) to `specs/features/FEAT-XXX-your-feature.md`.
2. **Define Contracts & Architecture**:
   - For interfaces or endpoints, define schemas in `specs/contracts/`.
   - For architectural choices, record an ADR in `specs/adr/`.
3. **Write Acceptance Tests**:
   Create tests in `tests/acceptance/` reflecting the BDD scenarios in your spec.
4. **Implement Code**:
   Build the functionality in `src/` until acceptance tests pass.
5. **Keep Specs in Sync**:
   Any deviation during implementation must be reflected back in the feature spec.

For a detailed walkthrough of the workflow, read [`docs/SDD_WORKFLOW.md`](docs/SDD_WORKFLOW.md).
