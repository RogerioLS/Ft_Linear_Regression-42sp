## 🎯 Objetivo Didático
Construir o segundo programa obrigatório da entrega: a CLI interativa de predição de preço.

## 📚 Regra de Negócio do Subject
Se `thetas.json` não existir (modelo ainda não treinado), o programa deve usar $\theta_0 = 0$ e $\theta_1 = 0$, retornando estimativa igual a $0.0$.

## 📝 Tarefas Técnicas
- [ ] Criar `predict.py` na raiz.
- [ ] Solicitar quilometragem via `input()` com validação de entradas não numéricas.
- [ ] Exibir o preço formatado em moeda/número legível.

## 🧪 Critérios de Aceite
- Teste 1: Rodar sem `thetas.json` ➔ Preço = $0.
- Teste 2: Rodar após `make train` ➔ Preço estimado coerente com o dataset.
