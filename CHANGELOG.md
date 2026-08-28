# Changelog

All notable changes to **42 ft_linear_regression** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

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
