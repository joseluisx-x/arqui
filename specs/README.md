# Specifications Directory (`specs/`)

This directory is the source of truth for all requirements, system architecture decisions, interfaces, and feature behaviors before code is written.

## Directory Structure

```text
specs/
├── adr/             # Architecture Decision Records (immutable history of technical decisions)
├── contracts/       # Machine-readable schemas (OpenAPI, JSON Schema, Protobuf, GraphQL)
├── features/        # Feature specifications, user stories, acceptance criteria
├── templates/       # Reusable templates for new specs and records
└── README.md        # This guide
```

## Spec-First Principles

1. **Spec Before Code**: No functional code is merged into `main` without an approved specification or update to an existing spec.
2. **Executable Acceptance Criteria**: Acceptance criteria should be written in Given-When-Then or clear assertive format so they directly translate to automated tests in `tests/acceptance/`.
3. **Living Documentation**: Specs evolve with the codebase. When requirements change, update the spec first.
4. **Contract-First Interfaces**: System interfaces and API endpoints must have their contracts defined in `specs/contracts/` before client/server implementation starts.

## How to Propose a New Feature

1. Copy `specs/templates/feature-spec-template.md` to `specs/features/FEAT-XXX-feature-name.md`.
2. Fill out Context, User Stories, and Acceptance Criteria.
3. If an API or schema change is required, draft the contract in `specs/contracts/`.
4. Submit a Pull Request / Review for spec sign-off.
5. Once approved, write automated acceptance tests in `tests/acceptance/` that fail initially (Red), then implement in `src/` to make them pass (Green).
