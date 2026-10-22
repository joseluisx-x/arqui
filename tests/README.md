# Tests Directory

In Spec-Driven Development (SDD), tests are categorized by how they validate requirements and specifications:

```text
tests/
├── acceptance/    # Validates specs/features/*.md (BDD / Scenario / End-to-End contracts)
├── integration/   # Validates multi-module interactions, database queries, and external APIs
├── unit/          # Validates individual domain models, utility functions, and business logic
└── README.md      # This guide
```

## Spec-Driven Test Workflow

1. **Acceptance Tests First (Red)**:
   - When a spec in `specs/features/` is approved, author acceptance tests in `tests/acceptance/` reflecting the Given-When-Then scenarios.
   - Run tests to confirm they fail (validating that the test itself works and the feature is not yet built).
2. **Unit & Integration Tests (TDD)**:
   - As you design modules in `src/`, author fine-grained unit and integration tests.
3. **Implementation (Green)**:
   - Implement the code in `src/` until all unit, integration, and acceptance tests pass.
4. **Refactor & Verify**:
   - Refactor code while keeping tests green and contracts intact.
