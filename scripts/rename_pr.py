#!/usr/bin/env python3
"""Rename Pull Request Title with 42 ft_linear_regression Audit Results.

Appends live audit status and deliverables count to the PR title via GitHub REST API.
Example: "feat(core): train.py | ✅ Audit 100% | 🛡️ Anti-Cheating OK | 🧪 5/5 Tests"
"""

import json
import os
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
METRICS_PATH = BASE_DIR / "artifacts" / "audit_summary.json"


def main() -> None:
    """Updates the PR title with the latest audit results."""
    event_path = os.getenv("GITHUB_EVENT_PATH")
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")

    if not event_path or not token or not repo or not os.path.exists(event_path):
        print("ℹ️ Skipping PR rename: Not running inside a PR workflow or missing tokens.")
        return

    with open(event_path, "r", encoding="utf-8") as f:
        event_data = json.load(f)

    if "pull_request" not in event_data or not METRICS_PATH.exists():
        return

    pr_number = event_data["pull_request"]["number"]
    raw_title = event_data["pull_request"]["title"]

    clean_title = raw_title.split(" | ✅ Audit")[0].split(" | ⚠️ Audit")[0].strip()

    with open(METRICS_PATH, "r", encoding="utf-8") as f:
        metrics = json.load(f)

    overall_passed = metrics.get("overall_passed", False)
    norm_errors = metrics.get("norm_errors", 0)
    passed_tests = metrics.get("passed_tests", 0)
    total_tests = metrics.get("total_tests", 0)
    implemented_count = metrics.get("implemented_deliverables", 0)

    if overall_passed:
        status_tag = (
            f"✅ Audit 100% | 🛡️ Anti-Cheating OK | 🧪 {passed_tests}/{total_tests} Tests "
            f"| 📦 {implemented_count}/3 Deliverables"
        )
    else:
        status_tag = f"⚠️ Audit Failed | 🛡️ Norm {norm_errors} Error(s)"

    new_title = f"{clean_title} | {status_tag}"
    if new_title == raw_title:
        print("ℹ️ PR title is already up to date.")
        return

    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "42-ft-linear-regression-PR-Renamer",
    }
    data = json.dumps({"title": new_title}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="PATCH")

    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status == 200:
                print(f"✅ PR #{pr_number} title updated successfully to: {new_title}")
            else:
                print(f"⚠️ Failed to update PR title: HTTP {resp.status}")
    except Exception as e:
        print(f"⚠️ Error updating PR title via API: {e}")


if __name__ == "__main__":
    main()
