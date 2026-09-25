"""Integration tests for predict.py CLI in ft_linear_regression."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from predict import estimate_price, load_thetas, run_prediction, validate_mileage_input


class TestPredictCLI(unittest.TestCase):
    """Integration test suite for price estimation inference engine."""

    def setUp(self) -> None:
        """Sets up test directory and environment."""
        self.root_dir = Path(__file__).resolve().parent.parent.parent
        self.predict_script = self.root_dir / "predict.py"
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        """Cleans up temporary resources."""
        self.temp_dir.cleanup()

    def test_load_thetas_missing_file_fallback(self) -> None:
        """Verifies missing thetas file defaults to 0.0 and untrained status."""
        missing = self.temp_path / "non_existent.json"
        th0, th1, is_trained = load_thetas(missing)
        self.assertEqual(th0, 0.0)
        self.assertEqual(th1, 0.0)
        self.assertFalse(is_trained)

    def test_load_thetas_valid_file(self) -> None:
        """Verifies loading parameters from valid JSON file."""
        thetas_file = self.temp_path / "thetas.json"
        with open(thetas_file, "w", encoding="utf-8") as f:
            json.dump({"theta0": 8500.0, "theta1": -0.02}, f)

        th0, th1, is_trained = load_thetas(thetas_file)
        self.assertEqual(th0, 8500.0)
        self.assertEqual(th1, -0.02)
        self.assertTrue(is_trained)

    def test_load_thetas_corrupted_file(self) -> None:
        """Verifies corrupted JSON defaults to 0.0 without raising unhandled error."""
        corrupted = self.temp_path / "corrupted.json"
        corrupted.write_text("invalid json syntax", encoding="utf-8")
        th0, th1, is_trained = load_thetas(corrupted)
        self.assertEqual(th0, 0.0)
        self.assertEqual(th1, 0.0)
        self.assertFalse(is_trained)

    def test_estimate_price_zero_thetas(self) -> None:
        """Verifies price is exactly 0.0 when model is untrained."""
        price = estimate_price(150000.0, 0.0, 0.0)
        self.assertEqual(price, 0.0)

    def test_estimate_price_linear_formula(self) -> None:
        """Verifies linear formula h(x) = theta0 + (theta1 * x)."""
        price = estimate_price(100000.0, 8000.0, -0.02)
        self.assertAlmostEqual(price, 6000.0)

    def test_validate_mileage_input_valid(self) -> None:
        """Verifies valid numeric string conversions."""
        self.assertEqual(validate_mileage_input("100000"), 100000.0)
        self.assertEqual(validate_mileage_input(" 240000.50 "), 240000.5)
        self.assertEqual(validate_mileage_input("150,5"), 150.5)

    def test_validate_mileage_input_invalid_values(self) -> None:
        """Verifies ValueError raised on empty, non-numeric or negative inputs."""
        with self.assertRaises(ValueError):
            validate_mileage_input("")
        with self.assertRaises(ValueError):
            validate_mileage_input("not_a_number")
        with self.assertRaises(ValueError):
            validate_mileage_input("-500")

    def test_run_prediction_untrained_fallback(self) -> None:
        """Verifies programmatic execution returns 0.0 when model is untrained."""
        missing = self.temp_path / "untrained.json"
        price = run_prediction(thetas_path=missing, mileage=100000.0, verbose=False)
        self.assertEqual(price, 0.0)

    def test_run_prediction_trained(self) -> None:
        """Verifies programmatic execution with trained thetas."""
        thetas_file = self.temp_path / "thetas.json"
        with open(thetas_file, "w", encoding="utf-8") as f:
            json.dump({"theta0": 8481.17, "theta1": -0.02127}, f)

        price = run_prediction(thetas_path=thetas_file, mileage=100000.0, verbose=False)
        self.assertAlmostEqual(price, 8481.17 - (0.02127 * 100000.0), places=2)

    def test_cli_subprocess_untrained(self) -> None:
        """Verifies predict.py CLI without thetas prints UNTRAINED and predicts $ 0.00."""
        missing = self.temp_path / "missing.json"
        result = subprocess.run(
            [sys.executable, str(self.predict_script), "-t", str(missing)],
            input="100000\n",
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("UNTRAINED", result.stdout)
        self.assertIn("$ 0.00", result.stdout)

    def test_cli_subprocess_trained(self) -> None:
        """Verifies predict.py CLI with thetas outputs trained prediction."""
        thetas_file = self.temp_path / "thetas.json"
        with open(thetas_file, "w", encoding="utf-8") as f:
            json.dump({"theta0": 8481.17, "theta1": -0.02127}, f)

        result = subprocess.run(
            [
                sys.executable,
                str(self.predict_script),
                "-t",
                str(thetas_file),
                "-m",
                "100000",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("TRAINED", result.stdout)
        self.assertIn("$ 6,354.17", result.stdout)

    def test_cli_subprocess_negative_mileage_flag_error(self) -> None:
        """Verifies predict.py CLI returns exit code 1 when negative mileage flag passed."""
        result = subprocess.run(
            [
                sys.executable,
                str(self.predict_script),
                "-m",
                "-100",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Error: Mileage cannot be negative", result.stderr)


if __name__ == "__main__":
    unittest.main()
