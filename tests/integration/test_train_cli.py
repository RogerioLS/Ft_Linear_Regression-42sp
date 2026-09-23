"""Integration tests for train.py CLI in ft_linear_regression."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from train import DEFAULT_DATASET, parse_args, save_thetas, train_model


class TestTrainCLI(unittest.TestCase):
    """Integration test suite for model training and parameter persistence CLI."""

    def setUp(self) -> None:
        """Sets up test directory and file references."""
        self.root_dir = Path(__file__).resolve().parent.parent.parent
        self.dataset_path = self.root_dir / DEFAULT_DATASET
        self.train_script = self.root_dir / "train.py"
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        """Cleans up temporary resources."""
        self.temp_dir.cleanup()

    def test_save_thetas_writes_valid_json(self) -> None:
        """Verifies save_thetas writes correct JSON format and metadata."""
        dest = self.temp_path / "test_thetas.json"
        save_thetas(dest, 123.456, -0.789, {"epochs": 500})

        self.assertTrue(dest.exists())
        with open(dest, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertAlmostEqual(data["theta0"], 123.456)
        self.assertAlmostEqual(data["theta1"], -0.789)
        self.assertEqual(data["epochs"], 500)

    def test_train_model_programmatic(self) -> None:
        """Verifies train_model executes gradient descent and saves parameters."""
        output_file = self.temp_path / "thetas_test.json"
        th0, th1 = train_model(
            dataset_path=self.dataset_path,
            output_path=output_file,
            alpha=0.1,
            epochs=1000,
            verbose=False,
        )

        self.assertTrue(output_file.exists())
        self.assertGreater(th0, 8000.0)
        self.assertLess(th1, 0.0)

        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("theta0", data)
        self.assertIn("theta1", data)
        self.assertIn("initial_cost_norm", data)
        self.assertIn("final_cost_norm", data)
        self.assertLess(data["final_cost_norm"], data["initial_cost_norm"])

    def test_parse_args_defaults(self) -> None:
        """Verifies CLI argument parser uses expected default options."""
        args = parse_args([])
        self.assertEqual(args.dataset, "dataset/data.csv")
        self.assertEqual(args.output, "thetas.json")
        self.assertEqual(args.alpha, 0.1)
        self.assertEqual(args.epochs, 1000)

    def test_parse_args_custom(self) -> None:
        """Verifies CLI argument parser handles explicit flags correctly."""
        args = parse_args(["my_data.csv", "-o", "out.json", "-a", "0.05", "-e", "500"])
        self.assertEqual(args.dataset, "my_data.csv")
        self.assertEqual(args.output, "out.json")
        self.assertEqual(args.alpha, 0.05)
        self.assertEqual(args.epochs, 500)

    def test_train_cli_execution_success(self) -> None:
        """Verifies train.py CLI process executes successfully with code 0."""
        output_file = self.temp_path / "cli_thetas.json"
        result = subprocess.run(
            [
                sys.executable,
                str(self.train_script),
                str(self.dataset_path),
                "-o",
                str(output_file),
                "-a",
                "0.1",
                "-e",
                "100",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("Model successfully trained!", result.stdout)
        self.assertTrue(output_file.exists())

    def test_train_cli_missing_file_error(self) -> None:
        """Verifies train.py CLI exits with code 1 when dataset is not found."""
        missing_csv = self.temp_path / "non_existent.csv"
        result = subprocess.run(
            [
                sys.executable,
                str(self.train_script),
                str(missing_csv),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Training Error", result.stderr)

    def test_train_cli_corrupted_dataset_error(self) -> None:
        """Verifies train.py CLI exits with code 1 when dataset has malformed header."""
        corrupted_csv = self.temp_path / "corrupted.csv"
        corrupted_csv.write_text("wrong_col1,wrong_col2\n10,20\n", encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable,
                str(self.train_script),
                str(corrupted_csv),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Training Error", result.stderr)


if __name__ == "__main__":
    unittest.main()
