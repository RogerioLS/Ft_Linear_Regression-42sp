# Copilot & Agent Instructions — 42 ft_linear_regression

This repository contains the complete implementation, tests, and peer-evaluation defense documentation for **ft_linear_regression (Car Price Prediction from Mileage)** at École 42 São Paulo.

---

## 🎯 Project Scope & Architecture

1. **Training Engine (`train.py` / `src/model/`)**:
   - Pure mathematical implementation of Batch Gradient Descent for univariate linear regression.
   - ⚠️ **Strict 42 Anti-Cheating**: Strictly prohibited to use `np.polyfit`, `LinearRegression`, or `curve_fit`.
   - Feature scaling (Min-Max / Z-score) with analytical unscaling to raw units ($\theta_0$ and $\theta_1$).
   - Persists trained parameters into `thetas.json`.

2. **Inference Engine (`predict.py`)**:
   - Interactive prompt asking the user for a car mileage in kilometers.
   - Calculates estimated price using $h_\theta(x) = \theta_0 + (\theta_1 \times x)$.
   - If `thetas.json` does not exist, defaults to $\theta_0=0, \theta_1=0$.

3. **Bonus Visualizations & Precision (`plot.py` / `scripts/evaluate_metrics.py`)**:
   - Scatter plot of mileage vs price with regression line.
   - Metrics: $R^2 \text{ Score}$, $MSE$, $RMSE$, $MAE$.

---

## 🛡️ 42 Principles & Standards

- Minimal, clean, and mathematically sound code.
- Explicit function and class docstrings (`__doc__`) on every function, class, and method.
- Main entrypoint guards (`if __name__ == "__main__":`) on all executable scripts.
- Maximum line length of 100 characters adhering to Black and Flake8 standards.
- Verification via Makefile (`make audit`, `make norm`, `make test`, `make summary`).
