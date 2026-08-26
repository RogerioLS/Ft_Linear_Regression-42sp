# Mathematics & Algorithm Specifications

## 1. Linear Hypothesis
$$h_\theta(x) = \theta_0 + \theta_1 x$$

## 2. Cost Function (Mean Squared Error — MSE)
$$J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})^2$$

## 3. Simultaneous Gradient Descent Updates
$$\text{tmp}\theta_0 = \theta_0 - \alpha \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})$$
$$\text{tmp}\theta_1 = \theta_1 - \alpha \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$$
$$\theta_0 := \text{tmp}\theta_0, \quad \theta_1 := \text{tmp}\theta_1$$

## 4. Feature Scaling & Unscaling (De-normalization)
Due to large mileage values ($x \approx 240,000$), unscaled gradient descent diverges.
Using Min-Max Normalization:
$$x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}, \quad y_{norm} = \frac{y - y_{min}}{y_{max} - y_{min}}$$
After training $\theta_0^{norm}$ and $\theta_1^{norm}$, unscale back to original coordinates:
$$\theta_1 = \theta_1^{norm} \cdot \frac{y_{max} - y_{min}}{x_{max} - x_{min}}$$
$$\theta_0 = y_{min} + \theta_0^{norm} \cdot (y_{max} - y_{min}) - \theta_1 \cdot x_{min}$$
This ensures `predict.py` operates directly on raw kilometers without needing to carry scaling artifacts.
