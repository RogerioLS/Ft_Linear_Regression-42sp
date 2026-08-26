## 🎯 Objetivo Didático
Compreender a dedução do Gradiente Descendente a partir da minimização do Erro Quadrático Médio ($MSE$).

## 📚 Fórmulas do Subject
- **Hipótese Linear**: $h_\theta(x) = \theta_0 + \theta_1 x$
- **Função de Custo (MSE Loss)**:
  $$J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})^2$$
- **Derivadas Parciais (Gradientes)**:
  $$\frac{\partial J}{\partial \theta_0} = \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})$$
  $$\frac{\partial J}{\partial \theta_1} = \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$$

## ⚠️ Regra Anti-Cheating
Proibido usar `np.polyfit`, `LinearRegression` ou similares.

## 📝 Tarefas Técnicas
- [ ] Implementar classe `LinearRegression` em `src/model/linear_regression.py`.
- [ ] Implementar atualização simultânea com variáveis temporárias (`tmp_theta0`, `tmp_theta1`).

## 🧪 Critérios de Aceite
- Redução monotônica da função de custo $J(\theta)$ ao longo das iterações.
