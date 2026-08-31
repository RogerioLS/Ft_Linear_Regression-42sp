"""Unit tests for src.preprocessing.scaler module in ft_linear_regression."""

import unittest
from pathlib import Path

from src.preprocessing.loader import load_csv
from src.preprocessing.scaler import MinMaxScaler, denormalize_parameters


class TestMinMaxScaler(unittest.TestCase):
    """Test suite for handcrafted MinMaxScaler and analytical parameter denormalization."""

    def setUp(self) -> None:
        """Sets up test synthetic collections and dataset paths."""
        self.sample_data = [10.0, 20.0, 30.0, 40.0, 50.0]
        self.root_dir = Path(__file__).resolve().parent.parent.parent
        self.dataset_path = self.root_dir / "dataset" / "data.csv"

    def test_fit_bounds(self) -> None:
        """Verifies fit identifies exact min and max bounds."""
        scaler = MinMaxScaler().fit(self.sample_data)
        self.assertTrue(scaler.is_fitted)
        self.assertEqual(scaler.min_val, 10.0)
        self.assertEqual(scaler.max_val, 50.0)
        self.assertEqual(scaler.range_val, 40.0)

    def test_transform_bounds(self) -> None:
        """Verifies transform scales elements strictly into [0.0, 1.0]."""
        scaler = MinMaxScaler().fit(self.sample_data)
        scaled = scaler.transform(self.sample_data)
        self.assertEqual(scaled[0], 0.0)
        self.assertEqual(scaled[-1], 1.0)
        self.assertEqual(scaled[2], 0.5)

    def test_inverse_transform_reversibility(self) -> None:
        """Verifies inverse_transform recovers original values within 1e-9 precision."""
        km, _ = load_csv(self.dataset_path)
        scaler = MinMaxScaler().fit(km)
        scaled = scaler.transform(km)
        recovered = scaler.inverse_transform(scaled)

        for orig, rec in zip(km, recovered):
            self.assertAlmostEqual(orig, rec, places=9)

    def test_constant_data_edge_case(self) -> None:
        """Verifies scaler handles constant arrays without ZeroDivisionError."""
        constant_data = [42.0, 42.0, 42.0]
        scaler = MinMaxScaler().fit(constant_data)
        scaled = scaler.transform(constant_data)
        self.assertEqual(scaled, [0.0, 0.0, 0.0])
        recovered = scaler.inverse_transform(scaled)
        self.assertEqual(recovered, [42.0, 42.0, 42.0])

    def test_unfitted_scaler_raises(self) -> None:
        """Verifies transforming with unfitted scaler raises RuntimeError."""
        scaler = MinMaxScaler()
        with self.assertRaises(RuntimeError):
            scaler.transform([1.0, 2.0])
        with self.assertRaises(RuntimeError):
            scaler.inverse_transform([0.5])

    def test_denormalize_parameters_consistency(self) -> None:
        """Verifies analytical denormalization yields exact predictions."""
        km, price = load_csv(self.dataset_path)
        x_scaler = MinMaxScaler().fit(km)
        y_scaler = MinMaxScaler().fit(price)

        # Let arbitrary hypothesis in normalized space: y_norm = 0.2 + 0.6 * x_norm
        theta0_norm = 0.2
        theta1_norm = 0.6

        theta0_real, theta1_real = denormalize_parameters(
            theta0_norm, theta1_norm, x_scaler, y_scaler
        )

        for x_val in [km[0], km[10], km[-1]]:
            # Prediction in normalized space
            x_n = x_scaler.transform([x_val])[0]
            y_pred_n = theta0_norm + theta1_norm * x_n
            y_pred_recovered = y_scaler.inverse_transform([y_pred_n])[0]

            # Prediction in real space
            y_pred_real = theta0_real + theta1_real * x_val

            self.assertAlmostEqual(y_pred_recovered, y_pred_real, places=7)


if __name__ == "__main__":
    unittest.main()
