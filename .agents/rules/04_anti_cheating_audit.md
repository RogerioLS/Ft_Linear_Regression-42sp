# Anti-Cheating & Integrity Rules

The 42 subject explicitly states:
> "You are also free to use any libraries you want as long as they do not do all the work for you. For example, the use of Python’s numpy.polyfit is considered cheating."

### Prohibited in `ft_linear_regression`:
- `numpy.polyfit`, `numpy.poly1d`
- `sklearn.linear_model.LinearRegression`, `Ridge`, `Lasso`
- `scipy.optimize.curve_fit`, `scipy.stats.linregress`
- `statsmodels.api.OLS`

### Permitted:
- `numpy` for arrays and basic elementwise arithmetic (`+`, `-`, `*`, `/`, `np.mean` for MSE loss).
- `matplotlib` for generating the bonus regression line and scatter plots.
- Standard Library `math`, `json`, `sys`, `pathlib`.
