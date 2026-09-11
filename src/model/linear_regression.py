"""Linear Regression and Batch Gradient Descent Engine for 42 ft_linear_regression.

Implements univariate linear regression from first mathematical principles without
third-party estimators or solvers (zero-cheating compliance with 42 curriculum).
"""

from typing import List, Tuple, Union

import numpy as np


class LinearRegression:
    """Handcrafted Simple Linear Regression trained via Batch Gradient Descent.

    Computes optimal slope (theta1) and intercept (theta0) to fit a linear
    hypothesis to univariate feature data: h_theta(x) = theta0 + (theta1 * x).
    """

    def __init__(self, theta0: float = 0.0, theta1: float = 0.0) -> None:
        """Initializes model parameters with zero or user-provided values.

        Args:
            theta0 (float): Initial intercept / bias term. Defaults to 0.0.
            theta1 (float): Initial slope / weight term. Defaults to 0.0.
        """
        self.theta0: float = float(theta0)
        self.theta1: float = float(theta1)
        self.cost_history: List[float] = []

    @property
    def thetas(self) -> Tuple[float, float]:
        """Returns the current model parameters as a tuple (theta0, theta1).

        Returns:
            Tuple[float, float]: Model intercept and slope.
        """
        return self.theta0, self.theta1

    def predict(self, x: Union[float, int, List[float], np.ndarray]) -> Union[float, np.ndarray]:
        """Estimates target values using the linear hypothesis: y_hat = theta0 + theta1 * x.

        Args:
            x (Union[float, int, List[float], np.ndarray]): Input feature values.

        Returns:
            Union[float, np.ndarray]: Predicted values matching input shape.
        """
        if isinstance(x, (int, float, np.number)):
            return float(self.theta0 + (self.theta1 * float(x)))

        arr_x = np.asarray(x, dtype=np.float64)
        return self.theta0 + (self.theta1 * arr_x)

    def compute_cost(
        self,
        x: Union[List[float], np.ndarray],
        y: Union[List[float], np.ndarray],
    ) -> float:
        """Calculates Mean Squared Error (MSE Loss) cost function J(theta0, theta1).

        Formula:
            J(theta0, theta1) = (1 / (2 * m)) * sum((h_theta(x^(i)) - y^(i))^2)

        Args:
            x (Union[List[float], np.ndarray]): Feature input array.
            y (Union[List[float], np.ndarray]): Target output array.

        Returns:
            float: Half Mean Squared Error cost value.

        Raises:
            ValueError: If inputs are empty or have unequal lengths.
        """
        arr_x = np.asarray(x, dtype=np.float64).ravel()
        arr_y = np.asarray(y, dtype=np.float64).ravel()

        if arr_x.size == 0 or arr_y.size == 0:
            raise ValueError("Cannot compute cost on empty input arrays.")
        if arr_x.size != arr_y.size:
            raise ValueError(
                f"Feature array ({arr_x.size}) and target array ({arr_y.size}) "
                f"must have the same length."
            )

        m = float(arr_x.size)
        predictions = self.predict(arr_x)
        errors = predictions - arr_y
        cost = (1.0 / (2.0 * m)) * float(np.sum(errors**2))
        return cost

    def compute_gradient(
        self,
        x: Union[List[float], np.ndarray],
        y: Union[List[float], np.ndarray],
    ) -> Tuple[float, float]:
        """Calculates analytical partial derivatives of cost function J with respect to thetas.

        Formulas:
            dJ/dtheta0 = (1 / m) * sum(h_theta(x^(i)) - y^(i))
            dJ/dtheta1 = (1 / m) * sum((h_theta(x^(i)) - y^(i)) * x^(i))

        Args:
            x (Union[List[float], np.ndarray]): Feature input array.
            y (Union[List[float], np.ndarray]): Target output array.

        Returns:
            Tuple[float, float]: Partial derivatives (grad0, grad1).

        Raises:
            ValueError: If inputs are empty or have unequal lengths.
        """
        arr_x = np.asarray(x, dtype=np.float64).ravel()
        arr_y = np.asarray(y, dtype=np.float64).ravel()

        if arr_x.size == 0 or arr_y.size == 0:
            raise ValueError("Cannot compute gradients on empty input arrays.")
        if arr_x.size != arr_y.size:
            raise ValueError(
                f"Feature array ({arr_x.size}) and target array ({arr_y.size}) "
                f"must have the same length."
            )

        m = float(arr_x.size)
        predictions = self.predict(arr_x)
        errors = predictions - arr_y

        grad0 = (1.0 / m) * float(np.sum(errors))
        grad1 = (1.0 / m) * float(np.sum(errors * arr_x))

        return grad0, grad1

    def fit(
        self,
        x: Union[List[float], np.ndarray],
        y: Union[List[float], np.ndarray],
        alpha: float = 0.1,
        epochs: int = 1000,
    ) -> "LinearRegression":
        """Optimizes parameters theta0 and theta1 using Batch Gradient Descent.

        Enforces simultaneous updates via temporary variables as specified in 42 subject:
            tmp_theta0 = theta0 - alpha * (1/m) * sum(error)
            tmp_theta1 = theta1 - alpha * (1/m) * sum(error * x)
            theta0 = tmp_theta0
            theta1 = tmp_theta1

        Args:
            x (Union[List[float], np.ndarray]): Normalized feature inputs.
            y (Union[List[float], np.ndarray]): Normalized target outputs.
            alpha (float): Learning rate. Must be positive. Defaults to 0.1.
            epochs (int): Number of training iterations. Must be >= 1. Defaults to 1000.

        Returns:
            LinearRegression: Trained instance for method chaining.

        Raises:
            ValueError: If alpha <= 0 or epochs < 1.
        """
        if alpha <= 0.0:
            raise ValueError(f"Learning rate alpha must be positive, got {alpha}.")
        if epochs < 1:
            raise ValueError(f"Number of epochs must be at least 1, got {epochs}.")

        arr_x = np.asarray(x, dtype=np.float64).ravel()
        arr_y = np.asarray(y, dtype=np.float64).ravel()

        if arr_x.size == 0 or arr_y.size == 0:
            raise ValueError("Training dataset cannot be empty.")
        if arr_x.size != arr_y.size:
            raise ValueError(
                f"Mismatch in feature size ({arr_x.size}) and target size ({arr_y.size})."
            )

        self.cost_history = []

        for _ in range(epochs):
            # 1. Record cost before current update
            current_cost = self.compute_cost(arr_x, arr_y)
            self.cost_history.append(current_cost)

            # 2. Compute analytical gradients
            grad0, grad1 = self.compute_gradient(arr_x, arr_y)

            # 3. Simultaneous update via temporary variables
            tmp_theta0 = self.theta0 - (alpha * grad0)
            tmp_theta1 = self.theta1 - (alpha * grad1)

            self.theta0 = float(tmp_theta0)
            self.theta1 = float(tmp_theta1)

        # Record final cost after all epochs completed
        final_cost = self.compute_cost(arr_x, arr_y)
        self.cost_history.append(final_cost)

        return self

    def __repr__(self) -> str:
        """Formal string representation of the model state."""
        return (
            f"LinearRegression(theta0={self.theta0:.6f}, theta1={self.theta1:.6f}, "
            f"trained_epochs={len(self.cost_history)})"
        )

    def __str__(self) -> str:
        """Readable mathematical hypothesis equation."""
        sign = "+" if self.theta1 >= 0 else "-"
        return f"h_theta(x) = {self.theta0:.4f} {sign} {abs(self.theta1):.4f} * x"
