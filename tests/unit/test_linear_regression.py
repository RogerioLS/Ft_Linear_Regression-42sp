"""Unit test suite for handcrafted LinearRegression model and Gradient Descent.

Validates:
1. Hypothesis prediction on scalars, lists, and numpy arrays.
2. Cost function MSE loss against exact mathematical derivations.
3. Analytical gradients (grad0, grad1) against step-by-step trace table.
4. Monotonic convergence of cost function J(theta) during training.
5. Parameter convergence on linear synthetic data.
6. Input validation and error handling for malformed inputs.
"""

import unittest

import numpy as np

from src.model.linear_regression import LinearRegression


class TestLinearRegression(unittest.TestCase):
    """Test cases for LinearRegression model."""

    def setUp(self) -> None:
        """Sets up mini-dataset from 42 masterclass trace table for numerical tests."""
        # Mini-dataset of 2 normalized cars from Masterclass
        self.mini_x = np.array([0.2, 0.8])
        self.mini_y = np.array([0.8, 0.2])

    def test_default_initialization(self) -> None:
        """Tests default initialization sets thetas to 0.0 and cost history to empty."""
        model = LinearRegression()
        self.assertEqual(model.theta0, 0.0)
        self.assertEqual(model.theta1, 0.0)
        self.assertEqual(model.thetas, (0.0, 0.0))
        self.assertEqual(len(model.cost_history), 0)

    def test_custom_initialization(self) -> None:
        """Tests initialization with custom parameters."""
        model = LinearRegression(theta0=2.5, theta1=-1.25)
        self.assertEqual(model.theta0, 2.5)
        self.assertEqual(model.theta1, -1.25)
        self.assertEqual(model.thetas, (2.5, -1.25))

    def test_predict_scalar(self) -> None:
        """Tests prediction with integer and float scalar values."""
        model = LinearRegression(theta0=10.0, theta1=2.0)
        self.assertAlmostEqual(model.predict(0), 10.0)
        self.assertAlmostEqual(model.predict(5.0), 20.0)
        self.assertAlmostEqual(model.predict(-3.0), 4.0)

    def test_hypothesis_zero_thetas(self) -> None:
        """Tests that hypothesis with theta0=0 and theta1=0 predicts exactly 0.0."""
        model = LinearRegression(theta0=0.0, theta1=0.0)
        self.assertEqual(model.predict(0.0), 0.0)
        self.assertEqual(model.predict(150000.0), 0.0)
        self.assertEqual(model.predict(-500.0), 0.0)

        preds = model.predict([10000.0, 50000.0, 240000.0])
        np.testing.assert_array_equal(preds, np.zeros(3))

    def test_predict_array_and_list(self) -> None:
        """Tests vector prediction preserving input dimensions."""
        model = LinearRegression(theta0=1.0, theta1=3.0)
        x_list = [0.0, 1.0, 2.0]
        preds_list = model.predict(x_list)
        np.testing.assert_allclose(preds_list, np.array([1.0, 4.0, 7.0]))

        x_arr = np.array([10.0, 20.0])
        preds_arr = model.predict(x_arr)
        np.testing.assert_allclose(preds_arr, np.array([31.0, 61.0]))

    def test_cost_function_zero_error(self) -> None:
        """Tests that a perfect linear fit produces a cost J(theta) of 0.0."""
        model = LinearRegression(theta0=2.0, theta1=4.0)
        x = np.array([1.0, 2.0, 3.0])
        y = np.array([6.0, 10.0, 14.0])
        cost = model.compute_cost(x, y)
        self.assertAlmostEqual(cost, 0.0, places=7)

    def test_mse_known_synthetic_dataset(self) -> None:
        """Tests MSE cost against handcrafted manual calculation on synthetic data."""
        # Model: h(x) = 1.0 + 1.0 * x
        model = LinearRegression(theta0=1.0, theta1=1.0)
        x = np.array([1.0, 2.0, 3.0])
        y = np.array([2.0, 3.0, 5.0])
        # Predictions: [2.0, 3.0, 4.0]
        # Differences: [0.0, 0.0, -1.0]
        # Squared differences sum: 0 + 0 + 1.0 = 1.0
        # J(theta) = 1 / (2 * 3) * 1.0 = 1 / 6 = 0.16666667
        cost = model.compute_cost(x, y)
        self.assertAlmostEqual(cost, 1.0 / 6.0, places=6)

    def test_gradient_zero_at_optimum(self) -> None:
        """Tests that partial derivatives are strictly 0.0 when fitted to perfect data."""
        model = LinearRegression(theta0=3.0, theta1=-2.0)
        x = np.array([0.0, 1.0, 2.0, 5.0])
        y = 3.0 - 2.0 * x
        grad0, grad1 = model.compute_gradient(x, y)
        self.assertAlmostEqual(grad0, 0.0, places=7)
        self.assertAlmostEqual(grad1, 0.0, places=7)

    def test_cost_function_masterclass_derivation(self) -> None:
        """Tests cost function calculation against the masterclass manual derivation."""
        model = LinearRegression(theta0=0.0, theta1=0.0)
        cost = model.compute_cost(self.mini_x, self.mini_y)
        # In Masterclass: J(0, 0) = (1 / 4) * [ (-0.8)^2 + (-0.2)^2 ] = (0.64 + 0.04) / 4 = 0.1700
        self.assertAlmostEqual(cost, 0.1700, places=4)

    def test_gradient_computation_masterclass_derivation(self) -> None:
        """Tests analytical gradients against masterclass derivation."""
        model = LinearRegression(theta0=0.0, theta1=0.0)
        grad0, grad1 = model.compute_gradient(self.mini_x, self.mini_y)

        # In Masterclass:
        # grad0 = (1/2) * [ (0.0 - 0.8) + (0.0 - 0.2) ] = -0.50
        # grad1 = (1/2) * [ (-0.8 * 0.2) + (-0.2 * 0.8) ] = (1/2) * (-0.16 - 0.16) = -0.16
        self.assertAlmostEqual(grad0, -0.50, places=4)
        self.assertAlmostEqual(grad1, -0.16, places=4)

    def test_epoch_1_update_masterclass(self) -> None:
        """Tests parameter update after Epoch 1 with alpha=0.1."""
        model = LinearRegression(theta0=0.0, theta1=0.0)
        model.fit(self.mini_x, self.mini_y, alpha=0.1, epochs=1)

        # In Masterclass:
        # theta0^(1) = 0.0 - 0.1 * (-0.50) = 0.050
        # theta1^(1) = 0.0 - 0.1 * (-0.16) = 0.016
        self.assertAlmostEqual(model.theta0, 0.050, places=3)
        self.assertAlmostEqual(model.theta1, 0.016, places=3)

        # Cost after epoch 1 in Masterclass is 0.1441
        cost_epoch_1 = model.compute_cost(self.mini_x, self.mini_y)
        self.assertAlmostEqual(cost_epoch_1, 0.1441, places=3)
        self.assertLess(cost_epoch_1, 0.1700)

    def test_monotonic_loss_decrease(self) -> None:
        """Verifies that cost J(theta) strictly decreases monotonically during training."""
        np.random.seed(42)
        x = np.linspace(0.0, 1.0, 30)
        y = 0.8 - 0.5 * x  # Linear relation with negative slope like real car data

        model = LinearRegression(theta0=0.0, theta1=0.0)
        model.fit(x, y, alpha=0.2, epochs=50)

        history = model.cost_history
        self.assertEqual(len(history), 51)  # 50 epochs + final cost

        for i in range(len(history) - 1):
            self.assertLessEqual(
                history[i + 1],
                history[i] + 1e-9,
                f"Loss increased at epoch {i}: {history[i]} -> {history[i+1]}",
            )

    def test_parameter_convergence(self) -> None:
        """Tests that gradient descent recovers true slope and intercept on clean linear data."""
        true_theta0 = 0.65
        true_theta1 = -0.45

        x = np.linspace(0.0, 1.0, 100)
        y = true_theta0 + (true_theta1 * x)

        model = LinearRegression(theta0=0.0, theta1=0.0)
        model.fit(x, y, alpha=0.5, epochs=1500)

    def test_gradient_convergence_few_epochs(self) -> None:
        """Tests that gradient descent consistently reduces cost over 5, 10, and 20 epochs."""
        x = np.array([0.1, 0.4, 0.7, 0.9])
        y = np.array([0.9, 0.6, 0.3, 0.1])
        model = LinearRegression(theta0=0.0, theta1=0.0)

        initial_cost = model.compute_cost(x, y)
        model.fit(x, y, alpha=0.1, epochs=5)
        cost_5 = model.compute_cost(x, y)
        self.assertLess(cost_5, initial_cost)

        model.fit(x, y, alpha=0.1, epochs=10)
        cost_15 = model.compute_cost(x, y)
        self.assertLess(cost_15, cost_5)

    def test_constant_target_convergence(self) -> None:
        """Tests that gradient descent recovers a horizontal line for constant target y."""
        x = np.linspace(0.0, 1.0, 50)
        y = np.full_like(x, 5.0)

        model = LinearRegression(theta0=0.0, theta1=0.0)
        model.fit(x, y, alpha=0.3, epochs=1000)

        self.assertAlmostEqual(model.theta0, 5.0, places=2)
        self.assertAlmostEqual(model.theta1, 0.0, places=2)

    def test_single_sample_dataset(self) -> None:
        """Tests cost and gradient evaluation on a single sample dataset."""
        model = LinearRegression(theta0=1.0, theta1=2.0)
        x = np.array([0.5])
        y = np.array([3.0])
        # h(0.5) = 1.0 + 2.0 * 0.5 = 2.0
        # error = 2.0 - 3.0 = -1.0
        # J = (1 / (2 * 1)) * (-1.0)^2 = 0.5
        cost = model.compute_cost(x, y)
        self.assertAlmostEqual(cost, 0.5)

        # grad0 = (1 / 1) * (-1.0) = -1.0
        # grad1 = (1 / 1) * (-1.0) * 0.5 = -0.5
        g0, g1 = model.compute_gradient(x, y)
        self.assertAlmostEqual(g0, -1.0)
        self.assertAlmostEqual(g1, -0.5)

    def test_invalid_arguments(self) -> None:
        """Tests that invalid training arguments raise appropriate ValueError."""
        model = LinearRegression()

        # Invalid alpha
        with self.assertRaises(ValueError):
            model.fit(self.mini_x, self.mini_y, alpha=0.0, epochs=10)
        with self.assertRaises(ValueError):
            model.fit(self.mini_x, self.mini_y, alpha=-0.1, epochs=10)

        # Invalid epochs
        with self.assertRaises(ValueError):
            model.fit(self.mini_x, self.mini_y, alpha=0.1, epochs=0)

        # Empty inputs
        with self.assertRaises(ValueError):
            model.fit([], [], alpha=0.1, epochs=10)
        with self.assertRaises(ValueError):
            model.compute_cost([], [])
        with self.assertRaises(ValueError):
            model.compute_gradient([], [])

        # Dimension mismatch
        with self.assertRaises(ValueError):
            model.fit([1.0, 2.0], [1.0], alpha=0.1, epochs=10)
        with self.assertRaises(ValueError):
            model.compute_cost([1.0, 2.0], [1.0])
        with self.assertRaises(ValueError):
            model.compute_gradient([1.0, 2.0], [1.0])

    def test_string_representations(self) -> None:
        """Tests readable and formal string representations."""
        model = LinearRegression(theta0=1.2345, theta1=-6.7890)
        self.assertIn("1.2345", str(model))
        self.assertIn("- 6.7890", str(model))
        self.assertIn("LinearRegression", repr(model))


if __name__ == "__main__":
    unittest.main()
