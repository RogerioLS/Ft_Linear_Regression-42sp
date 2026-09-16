"""Unit Test Suite for scripts/create_pr.py Utility (42 ft_linear_regression).

Validates:
1. Extraction of task IDs and issue numbers from branch names and commit logs.
2. Parsing of local markdown issue definitions in .github/issues/.
3. Formatting of default automated PR title and markdown body.
4. Robust parsing of GitHub repository slugs from diverse origin URL formats.
"""

import unittest
from unittest.mock import MagicMock, patch

from scripts.create_pr import (
    extract_task_and_issue,
    generate_default_pr_content,
    get_repository_slug,
    read_issue_markdown,
)


class TestCreatePR(unittest.TestCase):
    """Unit tests for Pull Request automation helper functions."""

    def test_extract_task_and_issue_from_branch(self) -> None:
        """Tests task ID and issue number extraction from standard branch names."""
        task, issue = extract_task_and_issue("feat/lr-02-core-math-gradient")
        self.assertEqual(task, "LR-02")
        self.assertEqual(issue, 2)

        task, issue = extract_task_and_issue("feat/lr-01-data-pipeline")
        self.assertEqual(task, "LR-01")
        self.assertEqual(issue, 1)

        task, issue = extract_task_and_issue("chore/infra-setup")
        self.assertIsNone(task)
        self.assertIsNone(issue)

    def test_read_issue_markdown(self) -> None:
        """Tests that read_issue_markdown extracts title and objective for existing issue."""
        info = read_issue_markdown(2)
        self.assertIsNotNone(info)
        assert info is not None
        self.assertIn("title", info)
        self.assertIn("Gradient", info["title"])
        self.assertIn("objective", info)

    def test_read_issue_markdown_nonexistent(self) -> None:
        """Tests that read_issue_markdown returns None for non-existent issue number."""
        info = read_issue_markdown(999)
        self.assertIsNone(info)

    @patch("scripts.create_pr.collect_branch_commits")
    def test_generate_default_pr_content(self, mock_commits: MagicMock) -> None:
        """Tests synthesis of title and markdown body containing required sections."""
        mock_commits.return_value = [
            "✨ feat(model): [LR-02:#2] implement linear regression gradient descent",
            "✅ test(model): [LR-02:#2] add unit tests for cost decay",
        ]

        title, body = generate_default_pr_content("feat/lr-02-core-math-gradient")

        self.assertIn("LR-02", title)
        self.assertIn("## 🎯 Description & Subject Requirements", body)
        self.assertIn("### 📋 Key Deliverables & Commits", body)
        self.assertIn("### 🧪 Quality Gate", body)
        self.assertIn("Closes #2", body)
        self.assertIn("implement linear regression gradient descent", body)

    @patch("scripts.create_pr.get_git_output")
    def test_get_repository_slug_https(self, mock_git: MagicMock) -> None:
        """Tests extraction of owner and repository name from HTTPS origin URL."""
        mock_git.return_value = "https://github.com/RogerioLS/Ft_Linear_Regression-42sp.git"
        owner, repo = get_repository_slug()
        self.assertEqual(owner, "RogerioLS")
        self.assertEqual(repo, "Ft_Linear_Regression-42sp")

    @patch("scripts.create_pr.get_git_output")
    def test_get_repository_slug_ssh(self, mock_git: MagicMock) -> None:
        """Tests extraction of owner and repository name from SSH origin URL."""
        mock_git.return_value = "git@github.com:RogerioLS/Ft_Linear_Regression-42sp.git"
        owner, repo = get_repository_slug()
        self.assertEqual(owner, "RogerioLS")
        self.assertEqual(repo, "Ft_Linear_Regression-42sp")


if __name__ == "__main__":
    unittest.main()
