## 🎯 Objetivo Didático
Aprender por que dados com grandezas na casa de centenas de milhares ($km \approx 240.000$) causam divergência e overflow no Gradiente Descendente sem Feature Scaling.

## 📚 Conceito para Estudo em Dupla
Se multiplicamos a taxa de aprendizado $\alpha$ por uma quilometragem de $240.000$, o valor de $\theta_1$ explode em pouquíssimas iterações.
Com a normalização Min-Max:
$$x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}, \quad y_{norm} = \frac{y - y_{min}}{y_{max} - y_{min}}$$

Transformamos todos os dados para a escala $[0.0, 1.0]$, tornando a superfície de custo esférica e a convergência suave.

## 📝 Tarefas Técnicas
- [ ] Criar `src/preprocessing/scaler.py` com classe `MinMaxScaler` artesanal.
- [ ] Implementar métodos `fit`, `transform`, `inverse_transform`.
- [ ] Tratar leitura do CSV `dataset/data.csv` sem uso de bibliotecas de ML.

## 🧪 Critérios de Aceite
- Escala de $x$ e $y$ estritamente entre $0.0$ e $1.0$.
