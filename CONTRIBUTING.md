# Contributing Guidelines — 42 ft_linear_regression

Welcome to the **42 ft_linear_regression** repository! We follow rigorous software engineering, mathematical rigor, and clean code standards.

---

## 🛠️ Centralized Workflow with Makefile

We use an interactive **Makefile Command Center** to standardize all development, linting, testing, and execution tasks. Always prefer using `make` commands rather than invoking raw python commands:

| Command | Purpose | When to Use |
| :--- | :--- | :--- |
| `make help` | Displays the interactive command menu with descriptions | Anytime you need a quick command refresher |
| `make install` | Installs project dependencies in your local virtual environment | First-time project setup |
| `make check` | Runs full pre-commit linters and AST norm checks | **Before staging files or creating commits** |
| `make norm` | Audits docstrings, `__main__` guards, and AST anti-cheating rules | To verify strict 42 norm compliance |
| `make compile` | Verifies Python 3.10 syntax compilation across all files | Fast syntax validation |
| `make test` | Executes all unit and integration test suites recursively | After any code modification |
| `make audit` | Runs the full verification suite (`compile` + `norm` + `test`) | Before pushing or opening a Pull Request |
| `make summary` | Generates local Markdown audit report (`summary.md`) | To preview the PR audit comment locally |
| `make train` | Trains Linear Regression with Gradient Descent & saves thetas | Milestone 2 model training |
| `make predict` | Runs interactive / CLI mileage prediction with `thetas.json` | Milestone 2 inference verification |
| `make plot` | Displays bonus scatter plot and fitted regression line | Milestone 3 visual evaluation |
| `make evaluate` | Computes $R^2$, MSE, RMSE, and MAE precision bonus metrics | Milestone 3 bonus verification |
| `make clean` | Removes temporary cache files (`__pycache__`, `.pyc`, etc.) | Workspace hygiene |

---

## 🏷️ Branch, Commit & Task Naming Governance (Strict Enforcement)

To ensure full traceability between the **GitHub Kanban**, **Pull Requests**, and **Git History**, all branches and commit messages are strictly validated by automated hooks and GitHub Actions.

### 🌿 1. Branch Naming Format:
```text
<type>/<task-id>-<short-description-in-kebab-case>
```
- **Valid Examples**:
  - `feat/lr-01-data-pipeline`
  - `feat/lr-02-gradient-descent`
  - `fix/lr-04-learning-rate-divergence`
  - `docs/lr-07-peer-defense-guide`
  - `chore/infra-makefile-update`
- **Rejection Behavior**: If a branch name is invalid (e.g. `my-branch`, `test`, `dev`), the **GitHub Action (`branch_lint.yml`) will fail and block the Pull Request**.

---

### 📝 2. Commit Message Format:
```text
<type>(<scope>): [<TASK-ID>] <short description in lowercase>
```
- **Valid Task Examples**:
  - `feat(preprocessing): [LR-01] implement minmax scaler from scratch`
  - `feat(model): [LR-02] implement gradient descent batch training`
  - `feat(viz): [LR-03] plot regression line and cost curve`
  - `docs(theory): [LR-06] derive gradient and loss functions`
- **Valid Non-Task / Infrastructure Examples**:
  - `chore(build): [INFRA] configure pre-commit hooks and make check`
  - `docs(meta): [DOCS] update contributing guidelines and security policy`
  - `fix(types): [HOTFIX] resolve lint typing issue in script loader`

### 📋 Allowed Reserved Tags (for non-subject changes):
`[INFRA]`, `[CHORE]`, `[DOCS]`, `[FIX]`, `[HOTFIX]`, `[SECURITY]`, `[GLOBAL]`, `[CONFIG]`, `[DEPS]`

---

### 🔄 3. Dynamic Task Lifecycle & Auto-Sync:
1. **Local Dynamic Detection**: The `.githooks/commit-msg` dynamically checks `.github/issues/`. When a new file `lr-09-bonus.md` is added, the `[LR-09]` tag is **immediately valid** without editing any configuration!
2. **GitHub Web UI Sync**: If you or your peer open a new Issue on GitHub Web, simply run:
   ```bash
   make sync-tasks
   ```
   This downloads the new issue into `.github/issues/` so local git hooks recognize it offline.

---

### 🚨 4. Troubleshooting: What if my Commit or PR is Rejected?

- **If your commit was rejected by Git Hook**:
  ```text
  ⛔ COMMIT REJEITADO: TASK NÃO ENCONTRADA NO PROJETO
  ```
  1. Check if the task ID matches an existing file in `.github/issues/` (e.g. `[LR-01]` to `[LR-08]`);
  2. If it is a new task, create `.github/issues/lr-XX-title.md`;
  3. If it is a general improvement without a subject task, use `[INFRA]` or `[CHORE]`.

- **If your PR was rejected by Branch Lint Action**:
  Rename your local branch and update the remote:
  ```bash
  git branch -m <old-name> feat/<task-id>-<description>
  git push origin -u feat/<task-id>-<description>
  git push origin --delete <old-name>
  ```

---

## 🧪 Testing Pyramid Architecture

All tests must be placed in the `tests/` directory following this structure:
- `tests/unit/`: Tests individual mathematical functions in isolation (`src/preprocessing/scaler.py`, `src/model/regression.py`).
- `tests/integration/`: Tests end-to-end CLI behavior (`train.py`, `predict.py`, `plot.py`).

Execute all test suites with:
```bash
make test
```

---

## 🛡️ 42 Norm & Academic Integrity Rules

1. **Python 3.10 Compatibility**: Strictly use Python 3.10 standard library, NumPy, and Matplotlib.
2. **Line Length Limit**: Maximum **100 characters per line** enforced by Black, Flake8, and Ruff.
3. **Documentation**: Every module, class, and public function must have a complete docstring.
4. **Execution Guards**: All CLI scripts must be wrapped inside `if __name__ == "__main__":`.
5. **No Prohibited Built-in ML Libraries**:
   - `sklearn.linear_model`, `scipy.optimize.curve_fit`, `numpy.polyfit`, `statsmodels.OLS` are strictly forbidden in analytical code.
   - The Gradient Descent optimization algorithm and Hypothesis function must be implemented from scratch.

---

## 🚀 Pre-Push Checklist

Before pushing commits or opening a PR, ensure:
1. `make check` passes with zero errors;
2. `make audit` executes with 100% tests passing and 0 norm violations;
3. `CHANGELOG.md` is updated with your changes under `[Unreleased]`.
