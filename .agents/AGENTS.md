# AGENTS.md — 42 ft_linear_regression Agent Operating System

**Project:** 42 ft_linear_regression (Car Price Prediction from Mileage)
**Curriculum:** 42 São Paulo / 42 Network Specialization
**Python:** >= 3.10
**Purpose:** Master operating protocol for AI coding agents working in this repository
**Version:** 1.0

---

## 0. Why This File Exists

This file is the repository-level operating protocol for AI agents.
It defines:
- The exact delivery contract expected by 42 peer-evaluators;
- Mathematical boundaries and strict no-cheating rules (zero built-in fitting functions);
- The required files, formats, interactive CLIs, and bonus visualizers;
- Guidelines for peer-defense readiness.

---

## 1. Institutional Identity & Philosophy

You are operating as a strict 42 AI Coding Assistant.
- **Source of truth:** The subject PDF (`subject/en.subject.pdf`) and repository files.
- **Anti-Cheating:** It is strictly forbidden to use library functions that do the fitting for you (e.g. `np.polyfit`, `sklearn.linear_model.LinearRegression`, `scipy.optimize.curve_fit`). All gradient descent calculations and normalization must be computed from raw mathematical definitions.
- **Interactive Contract:** `predict.py` must prompt the user for input and fallback to $\theta_0=0, \theta_1=0$ if the model has not been trained yet.
- **Code Quality:** All functions/classes require complete docstrings, entrypoint guards, and PEP8/42 line length constraints ($\le 100$ chars).

---

## 2. Deliverable Requirements

| File | Type | Purpose | Mandatory Constraints |
|---|---|---|---|
| `train.py` | Executable CLI | Train Linear Regression & save weights | Batch Gradient Descent from scratch |
| `predict.py` | Executable CLI | Interactive terminal prediction | Prompts mileage; fallbacks to $\theta=0$ |
| `plot.py` | Executable CLI (Bonus) | Scatter plot + fitted line + cost curve | Visual verification of convergence |

---

## 3. Directory Architecture

- `src/preprocessing/`: Data normalization (`MinMaxScaler` or `StandardScaler`) to prevent gradient explosion.
- `src/model/`: Handcrafted Linear Regression & Gradient Descent optimizer.
- `src/visualization/`: Matplotlib plotting helpers for the fitted line and cost function curve.
- `tests/`: Automated unit test suites validating mathematical correctness.
- `scripts/`: AST norm checks, Git hooks, evaluation tools, PR summary generators.
- `docs/`: Mathematical derivations, formulas, defense checklists.
