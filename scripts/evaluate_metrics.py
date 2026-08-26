#!/usr/bin/env python3
"""Precision and Metrics Evaluator for 42 ft_linear_regression.

Calculates R^2 Score, Mean Squared Error (MSE), Root Mean Squared Error (RMSE),
and Mean Absolute Error (MAE) from scratch.
"""

import json
import math
import sys
from pathlib import Path


def load_dataset(csv_path: str) -> tuple[list[float], list[float]]:
    """Loads km and price columns from CSV dataset without high-level libraries."""
    km_list: list[float] = []
    price_list: list[float] = []

    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {csv_path}")

    lines = path.read_text(encoding="utf-8").strip().splitlines()
    if not lines:
        raise ValueError("Dataset is empty.")

    # Skip header
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split(",")
        if len(parts) >= 2:
            try:
                km_list.append(float(parts[0].strip()))
                price_list.append(float(parts[1].strip()))
            except ValueError:
                continue

    return km_list, price_list


def calculate_metrics(actual: list[float], predicted: list[float]) -> dict[str, float]:
    """Calculates R2, MSE, RMSE, and MAE from scratch.

    Args:
        actual: Real price values.
        predicted: Estimated price values.

    Returns:
        Dictionary containing r2, mse, rmse, and mae.
    """
    n = len(actual)
    if n == 0:
        return {"r2": 0.0, "mse": 0.0, "rmse": 0.0, "mae": 0.0}

    mean_actual = sum(actual) / n

    # Sum of Squared Residuals (SS_res) and Total Sum of Squares (SS_tot)
    ss_res = sum((y - y_hat) ** 2 for y, y_hat in zip(actual, predicted))
    ss_tot = sum((y - mean_actual) ** 2 for y in actual)

    r2 = 1.0 - (ss_res / ss_tot) if ss_tot != 0 else 0.0
    mse = ss_res / n
    rmse = math.sqrt(mse)
    mae = sum(abs(y - y_hat) for y, y_hat in zip(actual, predicted)) / n

    return {"r2": r2, "mse": mse, "rmse": rmse, "mae": mae}


def main() -> int:
    """Main execution function for evaluate_metrics."""
    if len(sys.argv) < 3:
        print("Usage: python3 scripts/evaluate_metrics.py <dataset.csv> <thetas.json>")
        return 1

    try:
        km_list, price_list = load_dataset(sys.argv[1])
        thetas_path = Path(sys.argv[2])

        theta0 = 0.0
        theta1 = 0.0
        if thetas_path.exists():
            with open(thetas_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                theta0 = float(data.get("theta0", 0.0))
                theta1 = float(data.get("theta1", 0.0))

        predicted = [theta0 + (theta1 * x) for x in km_list]
        metrics = calculate_metrics(price_list, predicted)

        print("==================================================")
        print(" 🎯  42 FT_LINEAR_REGRESSION PRECISION REPORT    ")
        print("==================================================")
        print(f"Theta 0 (Intercept):  {theta0:,.4f}")
        print(f"Theta 1 (Slope):      {theta1:,.6f}")
        print("--------------------------------------------------")
        print(f"R² Score (Precision): {metrics['r2'] * 100:.2f}% (R² = {metrics['r2']:.4f})")
        print(f"MSE  (Mean Sq Error): {metrics['mse']:,.2f}")
        print(f"RMSE (Root MSE):      {metrics['rmse']:,.2f}")
        print(f"MAE  (Mean Abs Err):  {metrics['mae']:,.2f}")
        print("==================================================")
        return 0
    except Exception as e:
        print(f"❌ Error during metrics evaluation: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
