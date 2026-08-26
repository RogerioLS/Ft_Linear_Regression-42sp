## 🎯 Objetivo Didático
Entender a matemática para converter os pesos treinados no espaço normalizado $[0, 1]$ de volta para as unidades originais ($km$ e $preço$).

## 📚 Dedução Matemática
Se $y_{norm} = \theta_0^{norm} + \theta_1^{norm} x_{norm}$, substituindo as fórmulas de Min-Max:
$$\theta_1 = \theta_1^{norm} \cdot \frac{y_{max} - y_{min}}{x_{max} - x_{min}}$$
$$\theta_0 = y_{min} + \theta_0^{norm} (y_{max} - y_{min}) - \theta_1 x_{min}$$

## 📝 Tarefas Técnicas
- [ ] Implementar método `unscale_thetas` em `src/preprocessing/scaler.py`.
- [ ] Salvar diretamente $\theta_0$ e $\theta_1$ desnormalizados no `thetas.json`.

## 🧪 Critérios de Aceite
- `predict.py` calcula o preço direto com $h_\theta(km) = \theta_0 + (\theta_1 \cdot km)$ sem precisar carregar o dataset.
