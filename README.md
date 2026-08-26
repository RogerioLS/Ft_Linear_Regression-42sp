# 🚗 42 ft_linear_regression — Car Price Prediction from Scratch

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Norm 42](https://img.shields.io/badge/norm-42%20compliant-success.svg)
![Target Precision](https://img.shields.io/badge/precision-R%C2%B2%20%E2%89%A5%2073%25-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-purple.svg)

*First Machine Learning Algorithm implementation from raw mathematical principles (Batch Gradient Descent).*

</div>

---

## 📖 Overview

This project implements a univariate **Linear Regression model from scratch** to predict the price of a car given its mileage.

### 🌟 Features:
- **Zero Built-In Fitting Libraries**: Handcrafted Gradient Descent without `np.polyfit`, `sklearn`, or `scipy`.
- **Feature Normalization**: Min-Max scaling with analytical de-normalization to eliminate gradient explosion on large mileages ($240,000\text{ km}$).
- **Interactive Prediction**: CLI with fallback defaults ($\theta_0=0, \theta_1=0$) prior to training.
- **Bonus Visualizations**: Scatter plot of observations, fitted regression line, and cost function convergence curve (`plot.py`).
- **Precision Metrics**: $R^2 \text{ Score}$, $MSE$, $RMSE$, and $MAE$ calculations (`make precision`).

---

## 📦 Deliverables Contract

| Program | Mandatory / Bonus | Command | Description |
|---|---|---|---|
| `train.py` | Mandatory | `make train` | Trains linear regression and saves `thetas.json` |
| `predict.py` | Mandatory | `make predict` | Interactive prompt for mileage price estimation |
| `plot.py` | Bonus | `make plot` | Plots data points and fitted regression line |
| `scripts/evaluate_metrics.py` | Bonus | `make precision` | Computes $R^2$, MSE, RMSE, and MAE |

---

## 🚀 Quickstart

```bash
# 1. Install dependencies
make install

# 2. Train the model
make train

# 3. Predict a price interactively
make predict

# 4. View the fitted line and dataset (Bonus)
make plot

# 5. Check precision metrics (Bonus)
make precision

# 6. Run full quality audit
make audit
```

---

## 👤 Author
* **Rogerio Silva** ([@RogerioLS](https://github.com/RogerioLS)) — *42 São Paulo* 🇧🇷
