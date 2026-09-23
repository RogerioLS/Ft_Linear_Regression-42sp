# Changelog

All notable changes to **42 ft_linear_regression** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

---

## [0.1.0] - 2026-09-18 — 01. Mathematical Foundations & Preprocessing

### ✨ Features & Algorithms
- [LR-03] Test Suite: Validação Unitária do Gradiente e Convergência ([#3](https://github.com/RogerioLS/Ft_Linear_Regression-42sp/issues/3)) by @RogerioLS
- [LR-02] Core Math: Hipótese, Custo MSE e Derivadas Parciais do Gradiente ([#2](https://github.com/RogerioLS/Ft_Linear_Regression-42sp/issues/2)) by @RogerioLS
- [LR-01] Data Pipeline: Leitura de CSV e Normalização Min-Max ([#1](https://github.com/RogerioLS/Ft_Linear_Regression-42sp/issues/1)) by @RogerioLS
### Added
- Modular packages scaffolding (`src/preprocessing/`, `src/model/`, `src/visualization/`).
- Automated AST Norm & Anti-Cheating checker (`scripts/norm_check.py`).
- Automated precision evaluation script (`scripts/evaluate_metrics.py`).
- Interactive ANSI Makefile Command Center with `make check`, `make audit`, `make summary`.
- Dual test suite architecture (`tests/unit/` and `tests/integration/`).
- GitHub CI/CD quality gate enforcement with dynamic PR naming and automated checklist updates.
- Structured GitHub Issue Templates in YAML (`bug_report.yml`, `task_request.yml`, `math_discussion.yml`).

---

## [1.0.0-rc1] - 2026-08-27

### Added
- Initial project architecture and governance setup.
- Official 42 subject specification and `dataset/data.csv`.
- Mathematical derivations documented in `docs/MATHEMATICS.md`.
- Peer evaluation defense walkthrough in `docs/PEER_EVALUATION_GUIDE.md`.
