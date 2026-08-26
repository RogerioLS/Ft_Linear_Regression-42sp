## 🎯 Objetivo Didático
Implementar o cálculo de precisão do modelo ($R^2$ Score) e preparar a dupla para a avaliação presencial da 42.

## 📚 Métricas Implementadas
- **Coeficiente de Determinação ($R^2$)**:
  $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$
- **MSE, RMSE e MAE**.

## 📝 Tarefas Técnicas
- [ ] Implementar `scripts/evaluate_metrics.py` com exibição formatada.
- [ ] Documentar o roteiro de perguntas no `docs/PEER_EVALUATION_GUIDE.md`.

## 🧪 Critérios de Aceite
- Execução: `make precision` exibindo $R^2 \approx 73\% \text{ a } 75\%$ no dataset fornecido.
