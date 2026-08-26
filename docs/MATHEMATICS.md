# 📐 42 ft_linear_regression — Mathematical Foundations

This document details the complete mathematical theory and step-by-step analytical derivations implemented in **ft_linear_regression**.

---

## 1. Problem Formulation

We are given a training dataset of $m$ observations:
$$\mathcal{D} = \{(x^{(0)}, y^{(0)}), (x^{(1)}, y^{(1)}), \dots, (x^{(m-1)}, y^{(m-1)})\}$$
where:
- $x^{(i)} \in \mathbb{R}$ is the mileage of car $i$ (in kilometers).
- $y^{(i)} \in \mathbb{R}$ is the actual price of car $i$ (in dollars/euros).
- $m$ is the total number of training samples ($m = 24$).

---

## 2. Hypothesis Function

We model the relationship between mileage $x$ and estimated price $\hat{y}$ as a linear hypothesis parameterized by $\theta_0$ (intercept) and $\theta_1$ (slope):

$$h_\theta(x) = \theta_0 + \theta_1 x$$

- $\theta_0$ represents the base price of a car with 0 km.
- $\theta_1$ represents the depreciation rate per kilometer traveled ($\theta_1 < 0$).

---

## 3. Cost Function (Mean Squared Error — MSE)

To quantify prediction error across all $m$ training examples, we define the cost function $J(\theta_0, \theta_1)$ as the Mean Squared Error:

$$J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})^2$$

*(The factor $\frac{1}{2}$ cancels out neatly when computing derivatives).*

---

## 4. Analytical Derivation of the Gradients

To find the minimum of $J(\theta)$, we compute its partial derivatives with respect to $\theta_0$ and $\theta_1$ using the Chain Rule:

### 4.1 Gradient with respect to $\theta_0$:
$$\frac{\partial J}{\partial \theta_0} = \frac{\partial}{\partial \theta_0} \left[ \frac{1}{2m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})^2 \right]$$
$$\frac{\partial J}{\partial \theta_0} = \frac{1}{2m} \sum_{i=0}^{m-1} 2(h_\theta(x^{(i)}) - y^{(i)}) \cdot \frac{\partial}{\partial \theta_0}(\theta_0 + \theta_1 x^{(i)} - y^{(i)})$$
$$\frac{\partial J}{\partial \theta_0} = \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})$$

### 4.2 Gradient with respect to $\theta_1$:
$$\frac{\partial J}{\partial \theta_1} = \frac{\partial}{\partial \theta_1} \left[ \frac{1}{2m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})^2 \right]$$
$$\frac{\partial J}{\partial \theta_1} = \frac{1}{2m} \sum_{i=0}^{m-1} 2(h_\theta(x^{(i)}) - y^{(i)}) \cdot \frac{\partial}{\partial \theta_1}(\theta_0 + \theta_1 x^{(i)} - y^{(i)})$$
$$\frac{\partial J}{\partial \theta_1} = \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$$

---

## 5. Batch Gradient Descent Update Rule

At each training iteration (epoch), we update $\theta_0$ and $\theta_1$ simultaneously in the direction of steepest descent scaled by the learning rate $\alpha$:

$$\theta_0 := \theta_0 - \alpha \frac{\partial J}{\partial \theta_0} = \theta_0 - \alpha \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})$$

$$\theta_1 := \theta_1 - \alpha \frac{\partial J}{\partial \theta_1} = \theta_1 - \alpha \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$$

---

## 6. Analytical Parameter De-normalization (Unscaling)

Because mileage values are large ($x \in [22899, 240000]$), gradient descent on raw coordinates either explodes (overflow) or requires an infinitesimally tiny $\alpha \approx 10^{-10}$.

We normalize features to $[0, 1]$ via Min-Max Scaling:
$$x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}, \quad y_{norm} = \frac{y - y_{min}}{y_{max} - y_{min}}$$

In normalized space, the hypothesis is:
$$y_{norm} = \theta_0^{norm} + \theta_1^{norm} x_{norm}$$

Substituting the normalization definitions:
$$\frac{y - y_{min}}{y_{max} - y_{min}} = \theta_0^{norm} + \theta_1^{norm} \left( \frac{x - x_{min}}{x_{max} - x_{min}} \right)$$

Multiplying by $(y_{max} - y_{min})$ and isolating $y$:
$$y = y_{min} + \theta_0^{norm}(y_{max} - y_{min}) + \theta_1^{norm} \frac{y_{max} - y_{min}}{x_{max} - x_{min}} (x - x_{min})$$

$$y = \underbrace{\left[ y_{min} + \theta_0^{norm}(y_{max} - y_{min}) - \theta_1^{norm} \frac{y_{max} - y_{min}}{x_{max} - x_{min}} x_{min} \right]}_{\theta_0} + \underbrace{\left[ \theta_1^{norm} \frac{y_{max} - y_{min}}{x_{max} - x_{min}} \right]}_{\theta_1} x$$

Therefore, the exact unscaled parameters in raw kilometers and dollars are:
$$\theta_1 = \theta_1^{norm} \cdot \frac{y_{max} - y_{min}}{x_{max} - x_{min}}$$
$$\theta_0 = y_{min} + \theta_0^{norm}(y_{max} - y_{min}) - \theta_1 \cdot x_{min}$$
