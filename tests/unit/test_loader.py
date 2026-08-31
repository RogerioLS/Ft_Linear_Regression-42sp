"""Unit tests for src.preprocessing.loader module in ft_linear_regression."""

import unittest
from pathlib import Path

from src.preprocessing.loader import load_csv


class TestDataLoader(unittest.TestCase):
    """Test suite for CSV dataset loader and data validation."""

    def setUp(self) -> None:
        """Sets up test dataset paths."""
        self.root_dir = Path(__file__).resolve().parent.parent.parent
        self.dataset_path = self.root_dir / "dataset" / "data.csv"

    def test_load_csv_success(self) -> None:
        """Verifies load_csv loads valid data.csv with 24 records."""
        km, price = load_csv(self.dataset_path)
        self.assertIsInstance(km, list)
        self.assertIsInstance(price, list)
        self.assertEqual(len(km), 24)
        self.assertEqual(len(price), 24)
        self.assertEqual(km[0], 240000.0)
        self.assertEqual(price[0], 3650.0)

    def test_load_csv_file_not_found(self) -> None:
        """Verifies FileNotFoundError on non-existent file."""
        missing = self.root_dir / "dataset" / "non_existent.csv"
        with self.assertRaises(FileNotFoundError):
            load_csv(missing)

    def test_load_csv_data_types(self) -> None:
        """Verifies all loaded elements are positive floats."""
        km, price = load_csv(self.dataset_path)
        for k in km:
            self.assertIsInstance(k, float)
            self.assertGreaterEqual(k, 0.0)
        for p in price:
            self.assertIsInstance(p, float)
            self.assertGreaterEqual(p, 0.0)


if __name__ == "__main__":
    unittest.main()
