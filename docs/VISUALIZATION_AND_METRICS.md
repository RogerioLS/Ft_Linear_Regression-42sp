# 📈 Visualização de Dados & Métricas de Avaliação (ft_linear_regression)

Este documento descreve a fundamentação matemática, interpretação gráfica e métricas de desempenho implementadas no projeto **ft_linear_regression**.

---

## 🎯 1. Visualizações Obrigatórias e Bônus (`plot.py`)

O executável `plot.py` gera duas análises visuais fundamentais:

### 1.1 Gráfico de Dispersão com Reta de Regressão Ajustada
- **Eixo X**: Quilometragem do veículo ($\text{km}$);
- **Eixo Y**: Preço do veículo ($\text{price}$);
- **Pontos Azuis**: Pares observados $(x^{(i)}, y^{(i)})$ extraídos de `dataset/data.csv`;
- **Reta Vermelha**: Hipótese ajustada $\hat{y} = \theta_0 + \theta_1 \cdot x$.
- **Interpretação**: A inclinação $\theta_1 < 0$ evidencia a desvalorização linear do automóvel à medida que sua quilometragem aumenta.

### 1.2 Curva de Convergência da Função de Custo ($J(\theta)$ vs. Épocas)
- **Eixo X**: Número de iterações / épocas do Gradiente Descendente;
- **Eixo Y**: Valor da função de custo Mean Squared Error ($J(\theta)$);
- **Interpretação**: Uma curva exponencial estritamente decrescente comprova que a taxa de aprendizado $\alpha$ foi calibrada adequadamente e que o algoritmo convergiu suavemente para o mínimo global sem oscilações caóticas.

---

## 🧮 2. Métricas de Avaliação e Precisão (`scripts/evaluate_metrics.py`)

### 2.1 Coeficiente de Determinação ($R^2$ Score)
Mede a proporção da variância da variável dependente que é previsível a partir da variável independente:

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum_{i=1}^m (y^{(i)} - \hat{y}^{(i)})^2}{\sum_{i=1}^m (y^{(i)} - \bar{y})^2}$$

* Onde $\bar{y} = \frac{1}{m}\sum y^{(i)}$ é a média dos preços reais.
* **Critério de Sucesso**: $R^2 \ge 0.70$ (indica que mais de $70\%$ da variabilidade do preço é explicada pela quilometragem).

### 2.2 Mean Squared Error ($MSE$)
$$MSE = \frac{1}{m} \sum_{i=1}^m (y^{(i)} - \hat{y}^{(i)})^2$$

### 2.3 Root Mean Squared Error ($RMSE$)
Mede a magnitude média do erro nas mesmas unidades do preço ($\$$):
$$RMSE = \sqrt{MSE}$$

### 2.4 Mean Absolute Error ($MAE$)
Mede a média das distâncias absolutas entre predição e valor real:
$$MAE = \frac{1}{m} \sum_{i=1}^m |y^{(i)} - \hat{y}^{(i)}|$$
