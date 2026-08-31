"""Feature Scaling and Min-Max Normalization module for 42 ft_linear_regression.

Implements a handcrafted MinMaxScaler to normalize unscaled features into [0.0, 1.0],
preventing gradient explosion during Gradient Descent, and provides exact analytical
denormalization methods to recover real-world theta parameters.
"""

from typing import Optional, Sequence


class MinMaxScaler:
    """Handcrafted Min-Max Scaler for 1D numerical sequences.

    Transforms features by scaling each feature to the range [0.0, 1.0].
    Formula:
        x_norm = (x - x_min) / (x_max - x_min)
    """

    def __init__(self) -> None:
        """Initializes uncalibrated MinMaxScaler."""
        self.min_val: Optional[float] = None
        self.max_val: Optional[float] = None
        self.range_val: Optional[float] = None
        self.is_fitted: bool = False

    def fit(self, data: Sequence[float]) -> "MinMaxScaler":
        """Computes minimum and maximum values from the input data.

        Args:
            data (Sequence[float]): Collection of numerical values.

        Returns:
            MinMaxScaler: The fitted scaler instance.

        Raises:
            ValueError: If input collection is empty.
        """
        if not data:
            raise ValueError("Cannot fit scaler on empty data collection.")

        self.min_val = float(data[0])
        self.max_val = float(data[0])

        for val in data:
            f_val = float(val)
            if f_val < self.min_val:
                self.min_val = f_val
            if f_val > self.max_val:
                self.max_val = f_val

        self.range_val = self.max_val - self.min_val
        self.is_fitted = True
        return self

    def transform(self, data: Sequence[float]) -> list[float]:
        """Scales numerical features into the range [0.0, 1.0].

        Args:
            data (Sequence[float]): Collection of numerical values to scale.

        Returns:
            list[float]: Scaled numerical values.

        Raises:
            RuntimeError: If scaler has not been fitted yet.
        """
        if not self.is_fitted or self.min_val is None or self.range_val is None:
            raise RuntimeError("Scaler must be fitted before transforming data.")

        # If constant data (min == max), scale to 0.0 to prevent division by zero
        if self.range_val == 0.0:
            return [0.0 for _ in data]

        return [(float(x) - self.min_val) / self.range_val for x in data]

    def fit_transform(self, data: Sequence[float]) -> list[float]:
        """Fits to data, then transforms it.

        Args:
            data (Sequence[float]): Collection of numerical values.

        Returns:
            list[float]: Scaled numerical values in range [0.0, 1.0].
        """
        return self.fit(data).transform(data)

    def inverse_transform(self, scaled_data: Sequence[float]) -> list[float]:
        """Reverses scaling operation back to original feature domain.

        Formula:
            x_original = x_scaled * (x_max - x_min) + x_min

        Args:
            scaled_data (Sequence[float]): Normalized numerical values.

        Returns:
            list[float]: Recovered values in original unscaled domain.

        Raises:
            RuntimeError: If scaler has not been fitted yet.
        """
        if not self.is_fitted or self.min_val is None or self.range_val is None:
            raise RuntimeError("Scaler must be fitted before inverse transforming.")

        if self.range_val == 0.0:
            return [self.min_val for _ in scaled_data]

        return [float(x_scaled) * self.range_val + self.min_val for x_scaled in scaled_data]


def denormalize_parameters(
    theta0_norm: float,
    theta1_norm: float,
    x_scaler: MinMaxScaler,
    y_scaler: MinMaxScaler,
) -> tuple[float, float]:
    """Analytically converts normalized regression weights to original domain thetas.

    Derivation:
        y_norm = theta0_norm + theta1_norm * x_norm
        (y - y_min) / Delta_y = theta0_norm + theta1_norm * ((x - x_min) / Delta_x)
        y = y_min + Delta_y * theta0_norm + (Delta_y / Delta_x) * theta1_norm * (x - x_min)
        theta1_real = theta1_norm * (Delta_y / Delta_x)
        theta0_real = y_min + theta0_norm * Delta_y - theta1_real * x_min

    Args:
        theta0_norm (float): Intercept parameter learned in normalized space.
        theta1_norm (float): Slope parameter learned in normalized space.
        x_scaler (MinMaxScaler): Scaler fitted on independent variable (km).
        y_scaler (MinMaxScaler): Scaler fitted on dependent variable (price).

    Returns:
        tuple[float, float]: Tuple containing (theta0_real, theta1_real).

    Raises:
        RuntimeError: If either scaler is uncalibrated.
        ZeroDivisionError: If x_scaler range is zero.
    """
    if not x_scaler.is_fitted or not y_scaler.is_fitted:
        raise RuntimeError("Both x_scaler and y_scaler must be fitted before denormalizing.")

    if x_scaler.range_val is None or x_scaler.min_val is None:
        raise RuntimeError("x_scaler contains invalid calibration bounds.")

    if y_scaler.range_val is None or y_scaler.min_val is None:
        raise RuntimeError("y_scaler contains invalid calibration bounds.")

    if x_scaler.range_val == 0.0:
        raise ZeroDivisionError("Cannot denormalize parameters when x feature range is zero.")

    delta_x = x_scaler.range_val
    delta_y = y_scaler.range_val
    x_min = x_scaler.min_val
    y_min = y_scaler.min_val

    theta1_real = theta1_norm * (delta_y / delta_x)
    theta0_real = y_min + (theta0_norm * delta_y) - (theta1_real * x_min)

    return theta0_real, theta1_real
