#!/usr/bin/env python3
"""Norm & Anti-Cheating Auditor for 42 ft_linear_regression.

Audits compliance with 42 evaluation rules:
1. All functions and classes must have docstrings (__doc__).
2. Executable scripts must use the `if __name__ == '__main__':` guard.
3. Syntax compilation check (Python 3.10).
4. Anti-Cheating check: Ensure linear regression logic does not call banned
   built-in fitting functions (np.polyfit, sklearn.linear_model.LinearRegression,
   scipy.optimize.curve_fit, statsmodels.api.OLS, etc.).
"""

import ast
import sys
from pathlib import Path

# Banned function / method names for linear regression calculation
BANNED_METHODS = {
    "polyfit",
    "LinearRegression",
    "curve_fit",
    "OrdinaryLeastSquares",
    "OLS",
    "linregress",
    "poly1d",
}


class AntiCheatingVisitor(ast.NodeVisitor):
    """AST visitor to detect calls to banned linear regression helper methods."""

    def __init__(self, filename: str) -> None:
        """Initializes the anti-cheating AST visitor.

        Args:
            filename (str): Name of the file being audited.
        """
        self.filename = filename
        self.violations: list[str] = []

    def visit_Call(self, node: ast.Call) -> None:
        """Inspects AST Call nodes for banned function or method names.

        Args:
            node (ast.Call): AST call node to inspect.
        """
        if isinstance(node.func, ast.Attribute):
            attr_name = node.func.attr
            if attr_name in BANNED_METHODS:
                self.violations.append(
                    f"Line {node.lineno}: Banned call '.{attr_name}()' detected!"
                )
        elif isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in BANNED_METHODS:
                self.violations.append(
                    f"Line {node.lineno}: Banned function '{func_name}()' detected!"
                )

        self.generic_visit(node)


def _check_docstrings(tree: ast.AST) -> tuple[list[str], list[str]]:
    """Validates module, class and function docstrings."""
    errors: list[str] = []
    warnings: list[str] = []

    if not ast.get_docstring(tree):
        warnings.append("Missing module-level docstring")

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not ast.get_docstring(node):
                errors.append(f"Function '{node.name}' is missing a docstring (__doc__)")
        elif isinstance(node, ast.ClassDef):
            if not ast.get_docstring(node):
                errors.append(f"Class '{node.name}' is missing a docstring (__doc__)")
            for subnode in node.body:
                if isinstance(
                    subnode, (ast.FunctionDef, ast.AsyncFunctionDef)
                ) and not ast.get_docstring(subnode):
                    errors.append(f"Method '{node.name}.{subnode.name}' is missing a docstring")

    return errors, warnings


def _check_main_guard(tree: ast.AST, filepath: Path) -> list[str]:
    """Ensures executable scripts contain the main guard."""
    for node in tree.body:
        if isinstance(node, ast.If) and isinstance(node.test, ast.Compare):
            left = node.test.left
            if isinstance(left, ast.Name) and left.id == "__name__":
                return []

    is_script = filepath.parent == filepath.parent.parent and filepath.suffix == ".py"
    if is_script and filepath.name != "__init__.py":
        return ["Executable script missing 'if __name__ == \"__main__\":' guard"]
    return []


def audit_file(filepath: Path, check_cheating: bool = True) -> tuple[list[str], list[str]]:
    """Audits a single Python file for 42 norm & clean code rules.

    Returns:
        tuple[list[str], list[str]]: (errors, warnings)
    """
    try:
        content = filepath.read_text(encoding="utf-8")
        tree = ast.parse(content, filename=str(filepath))
    except SyntaxError as e:
        return [f"SyntaxError: {e}"], []
    except Exception as e:
        return [f"ReadError: {e}"], []

    errors, warnings = _check_docstrings(tree)
    errors.extend(_check_main_guard(tree, filepath))

    if check_cheating:
        visitor = AntiCheatingVisitor(filepath.name)
        visitor.visit(tree)
        errors.extend(visitor.violations)

    return errors, warnings


def main() -> int:
    """Runs the full audit across the ft_linear_regression codebase."""
    root_dir = Path(__file__).resolve().parent.parent

    target_files = [
        *list(root_dir.glob("*.py")),
        *list((root_dir / "src").rglob("*.py")),
        *list((root_dir / "scripts").rglob("*.py")),
        *list((root_dir / "tests").rglob("*.py")),
    ]

    total_files = 0
    total_errors = 0
    total_warnings = 0

    print("==================================================")
    print(" 🛡️  42 FT_LINEAR_REGRESSION NORM & CODE AUDITOR  ")
    print("==================================================")

    for py_file in sorted(target_files):
        if not py_file.exists():
            continue
        if any(part in py_file.parts for part in (".venv", "venv", "__pycache__", "build", "dist")):
            continue

        rel_path = py_file.relative_to(root_dir)
        check_cheating = py_file.name in ("train.py", "predict.py") or "model" in py_file.parts

        errs, warns = audit_file(py_file, check_cheating=check_cheating)
        total_files += 1
        total_errors += len(errs)
        total_warnings += len(warns)

        if errs or warns:
            print(f"\n📄 {rel_path}:")
            for err in errs:
                print(f"  ❌ ERROR:   {err}")
            for warn in warns:
                print(f"  ⚠️  WARNING: {warn}")
        else:
            print(f"  ✔ {rel_path} (OK)")

    print("\n--------------------------------------------------")
    print(
        f"Summary: {total_files} files checked | {total_errors} errors | {total_warnings} warnings"
    )
    print("--------------------------------------------------")

    if total_errors > 0:
        print("❌ Audit FAILED: Please fix the errors listed above.")
        return 1

    print("✅ Audit PASSED: All 42 norm & integrity checks validated!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
