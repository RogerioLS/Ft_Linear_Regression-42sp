# Peer Evaluation Defense Guide

During evaluation, be prepared to demonstrate:
1. **No-Cheating**: Show `src/model/linear_regression.py` proving no `polyfit` or `LinearRegression` library calls.
2. **Formulas & Mathematics**: Write and explain the partial derivatives of $J(\theta)$ with respect to $\theta_0$ and $\theta_1$.
3. **Simultaneous Updates**: Explain why $\theta_0$ and $\theta_1$ must be computed into temporary variables before updating.
4. **Feature Normalization**: Explain why unscaled kilometers cause gradient divergence or overflow, and how the unscaling math works.
5. **Interactive Execution**: Run `predict.py` with zero weights (fallback $=0$), then run `train.py`, then test `predict.py` with custom mileages.
6. **Bonus Visualizations**: Run `plot.py` and explain the regression line fit and $R^2$ precision score.
