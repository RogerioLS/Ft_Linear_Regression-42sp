# Contributing Guidelines — 42 ft_linear_regression

Thank you for collaborating on **ft_linear_regression**!

---

## 🌿 Branching Strategy

- `main`: Production-ready code, always passing `make audit`.
- `feat/<task-id>-<description>`: Feature branches for specific tasks (e.g. `feat/lr-01-data-pipeline`).
- `fix/<issue-id>-<description>`: Bug fixes and refactors.

---

## 🔒 Commit Conventions (Conventional Commits)

Commit messages must follow the format: `<type>(<scope>): <short description>`
- `feat`: New feature or algorithm logic.
- `fix`: Bug fix.
- `docs`: Documentation updates.
- `test`: Adding or modifying tests.
- `chore`: Tooling, linters, CI/CD changes.

---

## 🛡️ Pre-Push Quality Gate

Before submitting a PR, verify:
```bash
make compile   # Syntax validation
make norm      # 42 Norm & AST Anti-Cheating check
make test      # Unit test suites
make summary   # Local summary generation
```
All checks must pass with 0 errors.
