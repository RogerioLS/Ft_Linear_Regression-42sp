# 42 ft_linear_regression Delivery Contract

1. **Required Files in Root**:
   - `train.py`: Trains linear regression and saves parameters ($\theta_0$ and $\theta_1$) into a file.
   - `predict.py`: Prompts the user for a mileage value and outputs the predicted price.
   - `plot.py` (Bonus): Plots data points, fitted line, and cost curve.

2. **Prediction Formula**:
   $$\text{estimatePrice}(\text{mileage}) = \theta_0 + (\theta_1 \times \text{mileage})$$

3. **Fallback Requirement**:
   - If `predict.py` is executed before `train.py`, $\theta_0 = 0$ and $\theta_1 = 0$, yielding $\text{estimatePrice} = 0.0$.
