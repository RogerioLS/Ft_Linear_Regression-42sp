# 🛡️ 42 ft_linear_regression — Peer Evaluation Defense Guide

This guide prepares the developer for the 42 peer-evaluation defense.

---

## 🎯 Step-by-Step Defense Walkthrough

### 1. Code Integrity & Anti-Cheating (Strict Check)
- **Action**: Open `src/model/linear_regression.py` and `src/preprocessing/scaler.py`.
- **Key Point**: Show the evaluator that no machine learning libraries (`numpy.polyfit`, `sklearn.linear_model.LinearRegression`, `scipy.optimize.curve_fit`) are used.
- **Terminal**: Run `make norm` to prove the AST auditor passed with 0 errors.

### 2. Pre-Training Fallback Test
- **Action**: Run `make clean` to remove any existing `thetas.json`.
- **Action**: Run `python3 predict.py` and enter any mileage (e.g. `100000`).
- **Expected Output**: The program must output an estimated price of **0.0** (because $\theta_0=0, \theta_1=0$).

### 3. Training the Model
- **Action**: Run `python3 train.py dataset/data.csv` (or `make train`).
- **Expected Output**: Training completes, displays epoch losses and final unscaled thetas, and saves `thetas.json`.

### 4. Post-Training Prediction
- **Action**: Run `python3 predict.py` with several test mileages:
  - `0 km` $\rightarrow \approx 8,499$ (Intercept base price)
  - `100,000 km` $\rightarrow \approx 6,355$
  - `240,000 km` $\rightarrow \approx 3,353$

### 5. Bonus Visualizations & Precision
- **Action**: Run `python3 plot.py dataset/data.csv` (or `make plot`).
  - Displays the 24 scatter points in blue and the fitted regression line in red.
  - Displays the cost decay curve.
- **Action**: Run `make precision` (or `python3 scripts/evaluate_metrics.py dataset/data.csv thetas.json`).
  - Shows $R^2 \approx 73.3\%$, MSE, RMSE, and MAE.
