# 📋 Relatório Amplo de Progresso, Arquitetura e Continuidade (Handoff)

**Projeto:** 42 FT_LINEAR_REGRESSION — Previsão de Preços de Carros via Gradiente Descendente
**Instituição:** 42 São Paulo / 42 Network Specialization
**Data do Registro Inicial:** Segunda-feira, 31 de Agosto de 2026
**Última Atualização:** Terça-feira, 01 de Setembro de 2026
**Autor:** Rogerio Silva ([@RogerioLS](https://github.com/RogerioLS))
**Status Atual:** **Fase 0 Concluída & Masterclass Didática + CI/CD de Deploy 100% Concluídos — Pronto para Task LR-01 e LR-02**

---

## 🧭 1. Contexto e Objetivos Estratégicos

### 1.1 O Desafio ft_linear_regression da 42
O projeto **ft_linear_regression** consiste em implementar do zero uma **Regressão Linear Simples** univariada para prever o preço de um carro com base em sua quilometragem (`km` $\to$ `price`).

O projeto possui **2 executáveis obrigatórios**, **1 regra estrita de Anti-Cheating** e **1 suíte de bônus**:
1. **`predict.py`**:
   * Prompt interativo que solicita a quilometragem do veículo ao usuário e estima o preço utilizando os parâmetros $\theta_0$ (intercepto) e $\theta_1$ (inclinação):
     $$\text{estimatePrice}(\text{mileage}) = \theta_0 + (\theta_1 \cdot \text{mileage})$$
   * Caso o modelo ainda não tenha sido treinado (`thetas.json` ou `.csv` inexistente), deve inicializar $\theta_0 = 0$ e $\theta_1 = 0$, retornando preço estimado $0$.
2. **`train.py`**:
   * Lê o arquivo `dataset/data.csv` e treina o modelo utilizando **Gradiente Descendente em Lote (*Batch Gradient Descent*)**.
   * Ao convergir, exporta os parâmetros ótimos $\theta_0$ e $\theta_1$ para persistência.
3. **⚠️ Regra Fundamental de No-Cheating da 42**:
   * É estritamente proibido o uso de bibliotecas prontas de Machine Learning (ex.: Scikit-Learn, Statsmodels) ou solucionadores diretos de regressão (ex.: `np.polyfit`, `scipy.optimize`).
   * Todo o algoritmo de otimização e cálculo do gradiente deve ser derivado e codificado a partir dos primeiros princípios matemáticos.
4. **Bônus**:
   * `plot.py`: Visualização dos pontos de dados juntamente com a reta de regressão ajustada e gráfico de convergência da função de custo $J(\theta)$.
   * Avaliação de precisão: Implementação de métricas estatísticas ($R^2$, $MSE$, $RMSE$, $MAE$).

### 1.2 O Desafio Numérico do Feature Scaling (MinMaxScaler)
A quilometragem no dataset atinge valores da ordem de $240.000\text{ km}$, enquanto o preço está na ordem de $3.000$ a $8.000$.
Sem normalização de escala (*Feature Scaling*), a multiplicação da taxa de aprendizado $\alpha$ por $x^{(i)} \approx 240.000$ faz o gradiente de $\theta_1$ explodir para o infinito (`overflow / NaN`) em poucas iterações.

**Solução:**
1. Normalizamos $x$ e $y$ para o intervalo $[0.0, 1.0]$ via Min-Max:
   $$x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}, \quad y_{norm} = \frac{y - y_{min}}{y_{max} - y_{min}}$$
2. Executamos o Gradiente Descendente no espaço normalizado encontrando $\theta_0^{norm}$ e $\theta_1^{norm}$.
3. Desnormalizamos analiticamente os parâmetros para a escala real:
   $$\theta_1^{real} = \theta_1^{norm} \cdot \left(\frac{y_{max} - y_{min}}{x_{max} - x_{min}}\right)$$
   $$\theta_0^{real} = y_{min} + \theta_0^{norm} \cdot (y_{max} - y_{min}) - \theta_1^{real} \cdot x_{min}$$

---

## 🏛️ 2. Arquitetura do Repositório (Padrão 42 + Production AI)

O repositório espelha o padrão canônico do **Master Architectural Blueprint (`espec-42/README.md`)**:

```text
Ft_Linear_Regression-42sp/
├── .agents/                               # Sistema Operacional do Agente de IA para a 42
│   ├── AGENTS.md                          # Protocolo mestre de regras e limites da 42
│   └── rules/
│       ├── 00_global_rules.md             # Padrões de código, tipagem e docstrings (100 cols)
│       ├── 01_42_linear_contract.md       # Requisitos de entrega e executáveis da raiz
│       ├── 02_math_and_algorithms.md      # Fórmulas de Gradiente, Custo e Desnormalização
│       ├── 03_evaluation_defense.md       # Roteiro de perguntas da avaliação presencial
│       └── 04_anti_cheating_audit.md      # Proibições estritas (sem polyfit / sklearn)
├── .github/
│   ├── CODEOWNERS                         # Responsável pelo repositório
│   ├── copilot-instructions.md            # Instruções de contexto para LLMs e Copilot
│   ├── dependabot.yml                     # Atualização automática de dependências e actions
│   ├── labeler.yml                        # Mapeamento de pastas para labels no PR
│   ├── pull_request_template.md           # Template padrão para PRs com checklist de qualidade
│   ├── release.yml                        # Categorização automática de Release Notes no GitHub
│   ├── ISSUE_TEMPLATE/                    # Formulários estruturados de Issues em YAML
│   │   ├── bug_report.yml                 # Template para relato de bugs e falhas
│   │   ├── task_request.yml               # Template para novas tarefas e refatorações
│   │   ├── math_discussion.yml            # Template para debates de derivações matemáticas
│   │   └── config.yml                     # Links de contato e guias
│   ├── issues/                            # 8 Tasks detalhadas em Markdown para estudo offline
│   │   ├── lr-01-data-pipeline.md
│   │   ├── lr-02-core-math-gradient.md
│   │   ├── lr-03-test-suite.md
│   │   ├── lr-04-cli-train.md
│   │   ├── lr-05-cli-predict.md
│   │   ├── lr-06-denormalization-unscaling.md
│   │   ├── lr-07-bonus-cli-plot.md
│   │   └── lr-08-bonus-precision-defense.md
│   ├── scripts/
│   │   ├── 01_setup_labels_and_milestones.sh # Criação de Milestones e Labels
│   │   ├── 02_setup_kanban_tasks.sh       # Criação idempotente das issues via --body-file
│   │   └── setup_kanban.sh                # Master runner do Kanban
│   └── workflows/
│       ├── audit.yml                      # CI/CD: Checagem de sintaxe, 42 norm, testes e Hard Quality Gate
│       ├── branch_lint.yml                # Validador estrito de nomenclatura de branches
│       ├── deploy-pages.yml               # Deploy automatizado do Interactive Journey no GitHub Pages
│       └── labeler.yml                    # Auto-labeling de Pull Requests
├── .githooks/                             # Hooks Locais do Git
│   ├── commit-msg                         # Validador dinâmico de Task ID [LR-XX:#NUM] e Commits
│   ├── pre-commit                         # Executa norm_check.py e pre-commit antes do commit
│   └── prepare-commit-msg                 # Prepend automático de emojis (Conventional Commits)
├── dataset/                               # Dataset oficial fornecido pela 42
│   └── data.csv                           # 24 registros de km e price
├── docs/                                  # Documentação técnica e científica
│   ├── MATHEMATICS.md                     # Derivações matemáticas formais e gradientes
│   ├── VISUALIZATION_AND_METRICS.md       # Interpretação dos gráficos e métricas de precisão
│   ├── PEER_EVALUATION_GUIDE.md           # Checklist para o dia da defesa presencial
│   └── interactive_journey.html           # Masterclass didática interativa completa
├── notes/
│   └── README.md                          # Rascunhos e anotações livres da dupla
├── scripts/                               # Ferramentas auxiliares e auditoria
│   ├── install-hooks.sh                   # Configurador dos githooks locais
│   ├── norm_check.py                      # Auditor com AST Anti-Cheating (sem polyfit / sklearn)
│   ├── generate_summary.py                # Gerador do summary.md e JSON de métricas
│   ├── rename_pr.py                       # Renomeador dinâmico do PR via GitHub API
│   ├── sync_tasks.py                      # Auto-sincronizador de tasks com o GitHub Issues
│   ├── update_issue_checklist.py          # Robô que marca checkboxes [x] e fecha issues no audit
│   ├── update_pr_checklist.py             # Marcador automático de checkboxes [x] no PR
│   └── evaluate_metrics.py                # Script de validação de métricas (R2, MSE, MAE)
├── src/                                   # Pacote modular interno
│   ├── __init__.py
│   ├── preprocessing/                     # MinMaxScaler e carregador de dados
│   │   └── __init__.py
│   ├── model/                             # Regressão Linear & Gradiente Descendente
│   │   └── __init__.py
│   └── visualization/                     # Plots com Matplotlib
│       └── __init__.py
├── subject/
│   └── en.subject.pdf                     # PDF oficial da 42
├── tests/                                 # Pirâmide de Testes Automatizados
│   ├── __init__.py
│   ├── unit/                              # Testes unitários das funções matemáticas
│   │   └── __init__.py
│   └── integration/                       # Testes de integração de ponta a ponta dos CLIs
│       └── __init__.py
├── .gitignore                             # Ignora caches, ambientes virtuais e predições
├── .pre-commit-config.yaml                # Black (100 colunas), isort, flake8, ruff, detect-secrets
├── CHANGELOG.md                           # Histórico de versões (Keep a Changelog / SemVer)
├── CODE_OF_CONDUCT.md                     # Código de Conduta Contributor Covenant v2.1 em inglês
├── CONTRIBUTING.md                        # Guia de contribuição e governança detalhada
├── HANDOFF_PROGRESSO.md                   # Este documento de referência e continuidade
├── Makefile                               # Central de controle interativa formatada em ANSI
├── pyproject.toml                         # Metadados, empacotamento e dependências Python 3.10+
├── README.md                              # Documentação principal com badges e guia rápido
└── SECURITY.md                            # Política de segurança e reporte de vulnerabilidades
```

---

## 🛠️ 3. Inventário Detalhado do que foi Desenvolvido na Fase 0 (31/08/2026)

### 3.1 Automação do Terminal ([Makefile](file:///mnt/c/Users/rogerio.silva/projetos/espec-42/Ft_Linear_Regression-42sp/Makefile))
* `make help`: Exibe o menu interativo com todos os comandos disponíveis.
* `make install`: Instala as dependências em modo editável e configura os git hooks (`./scripts/install-hooks.sh`).
* `make check`: Executa validação sanitária completa pré-commit (norm auditor + todos os linters do pre-commit).
* `make sync-tasks`: Sincroniza tarefas novas criadas no GitHub Issues diretamente para a pasta `.github/issues/`.
* `make train`: Executa `python3 train.py dataset/data.csv`.
* `make predict`: Executa `python3 predict.py`.
* `make plot`: Executa `python3 plot.py dataset/data.csv`.
* `make precision`: Executa `python3 scripts/evaluate_metrics.py dataset/data.csv thetas.json`.
* `make test`: Roda todos os testes unitários e de integração (`unittest discover -s tests`).
* `make norm`: Executa a auditoria de normas 42 e verificador AST anti-cheating.
* `make compile`: Valida a sintaxe Python 3.10 em todos os arquivos `.py`.
* `make summary`: Gera o relatório local de auditoria (`summary.md`).
* `make audit`: Roda o ciclo completo (`compile` + `norm` + `test`).
* `make clean`: Remove caches (`__pycache__`, `.pytest_cache`, `thetas.json`, `thetas.csv`).

### 3.2 Auditoria AST & Anti-Cheating ([scripts/norm_check.py](file:///mnt/c/Users/rogerio.silva/projetos/espec-42/Ft_Linear_Regression-42sp/scripts/norm_check.py))
* Implementa um `ast.NodeVisitor` que analisa o código-fonte procurando chamadas proibidas (`polyfit`, `polyval`, `LinearRegression`, `scipy.optimize`, etc.).
* Exige docstrings completas em todos os módulos, classes e funções/métodos.
* Exige `if __name__ == '__main__':` em todos os executáveis de entrada.
* **Status atual:** 100% aprovado com 0 erros e 0 avisos em 14 arquivos verificados.

### 3.3 Governança Estrita de Branches, Commits e Tasks
* **Hook `.githooks/commit-msg`**: Valida o formato `<type>(<scope>): [<TASK-ID>:#<ISSUE_NUM>] <descrição>` com busca dinâmica em `.github/issues/`.
* **Workflow `.github/workflows/branch_lint.yml`**: Bloqueia branches fora do padrão (ex: `feat/lr-01-data-pipeline`).
* **Robô de Issue Checklist (`scripts/update_issue_checklist.py`)**: Marca checkboxes `[x]` e fecha a Issue no GitHub Kanban ao passar no `make audit`.

---

## 🌟 4. Incremento: Masterclass Didática Interativa & Deploy Web (01/09/2026)

### 4.1 Masterclass Didática Interativa ([docs/interactive_journey.html](file:///mnt/c/Users/rogerio.silva/projetos/espec-42/Ft_Linear_Regression-42sp/docs/interactive_journey.html))
Desenvolvimento de uma plataforma educacional interativa completa, standalone e cronológica cobrindo 100% dos requisitos fundamentais e bônus do Subject 42:
* **0. Dicionário de Símbolos**: Nivelamento prévio traduzindo $\theta_0, \theta_1, \hat{y}, e, J(\theta), \alpha$ com analogias do dia a dia.
* **1. O Problema & Hipótese Linear**: Base real de 24 carros (`dataset/data.csv`), reta $\hat{y} = \theta_0 + \theta_1 x$ e visualização gráfica via Canvas.
* **2. Normalização Min-Max**: Análise do overflow numérico, dedução da equação $[0.0, 1.0]$, cálculo com $\Delta x = 217.101\text{ km}$ e $\Delta y = \$4.640$, e simulador interativo de normalização.
* **3. Função de Custo $J(\theta)$ & Derivadas com Regra da Cadeia**: Metáfora da boneca russa (função composta $f(u) = u^2$), fórmula geral $\frac{df}{du} \cdot \frac{du}{d\theta}$, tabela de derivadas de fora e dentro, corte analítico do $\frac{1}{2}$ com o $2$, e regra de atualização simultânea.
* **4. A Lousa do Professor (Cálculo Numérico Manual)**: Mini-dataset de 2 carros normalizados ($x_1=0.2, y_1=0.8$ e $x_2=0.8, y_2=0.2$) com a resolução manual e passo a passo das **Épocas 1 e 2**, comprovando a queda matemática de $J(\theta)$ ($0.1700 \to 0.1441 \to 0.1235$), acompanhado da Tabela de Rastreio (*Trace Table*).
* **5. Laboratório Interativo (Live GD Simulator)**: Canvas dinâmico renderizando ao vivo o ajuste da reta, resíduos verticais de cada ponto, sliders de controle para $\alpha$, total de épocas e ajustes manuais.
* **6. A Ponte da Desnormalização ($\theta^{norm} \to \theta^{real}$)**: Dedução analítica de 4 passos com os dados finais ($\theta_1^{real} = -\$0.019556/\text{km}$, $\theta_0^{real} = \$8.051,09$).
* **7. Seção Bônus & Métricas de Avaliação**: As 4 métricas formais ($R^2=0.733, MAE=\$541,20, RMSE=\$672,85, MSE=452.727,10$) destrinchadas linha a linha (fórmula, cálculo exato com os 24 carros, o que respondem, prós e contras) e gráfico da **Curva de Loss $J(\theta)$** em 500 épocas.
* **8. Guia da Defesa Presencial**: As 4 perguntas capitais com respostas fundamentadas para a avaliação entre pares na 42.
* **Navegação em Grade Multi-Linhas**: Menu superior responsivo em Grid sem barra de rolagem lateral.

### 4.2 CI/CD de Deploy Automatizado ([.github/workflows/deploy-pages.yml](file:///mnt/c/Users/rogerio.silva/projetos/espec-42/Ft_Linear_Regression-42sp/.github/workflows/deploy-pages.yml))
* Pipeline do GitHub Actions que realiza o deploy automático do `docs/interactive_journey.html` diretamente para o **GitHub Pages** a cada push na `main`, gerando o `index.html` em tempo de build.

---

## 🚦 5. Estado Atual e Validação

* `make compile` ➔ **PASSED (Sintaxe Python 3.10 validada em todos os arquivos)**.
* `make norm` ➔ **PASSED (14 arquivos auditados, 0 erros, 0 avisos)**.
* `make check` ➔ **PASSED (Black, Isort, Flake8, Ruff e Detect-Secrets verdes)**.
* `git status` ➔ **Pronto para iniciar as Tasks [LR-01] e [LR-02]**.

---

## 🚀 6. Roteiro Passo a Passo para as Tasks de Implementação

### 📋 Mapeamento Sequencial das Tasks:

| Task ID | Nome da Tarefa | Arquivos de Código | Arquivos de Teste |
| :---: | :--- | :--- | :--- |
| **`[LR-01]`** | **Data Pipeline & MinMaxScaler** | `src/preprocessing/scaler.py`, `src/preprocessing/loader.py` | `tests/unit/test_scaler.py`, `tests/unit/test_loader.py` |
| **`[LR-02]`** | **Core Math & Gradient Descent** | `src/model/linear_regression.py` | `tests/unit/test_linear_regression.py` |
| **`[LR-03]`** | **Test Suite & Verification** | Integração com ground truth | `tests/integration/test_model_accuracy.py` |
| **`[LR-04]`** | **CLI Training Engine (`train.py`)** | `train.py` (raiz) | `tests/integration/test_cli_train.py` |
| **`[LR-05]`** | **CLI Inference Engine (`predict.py`)** | `predict.py` (raiz) | `tests/integration/test_cli_predict.py` |
| **`[LR-06]`** | **Denormalization Math** | `src/preprocessing/scaler.py` | `tests/unit/test_denormalization.py` |
| **`[LR-07]`** | **Bonus Visualization (`plot.py`)** | `plot.py` (raiz), `src/visualization/plotter.py` | `tests/unit/test_plotter.py` |
| **`[LR-08]`** | **Bonus Evaluation Metric ($R^2$)** | `scripts/evaluate_metrics.py` | `tests/unit/test_metrics.py` |

---

## 📌 Checklist Rápido de Comandos

| Objetivo | Comando |
|---|---|
| Menu Interativo | `make help` |
| Sanity Check Pré-Commit | `make check` |
| Auditor de Normas 42 | `make norm` |
| Rodar Testes Unitários | `make test` |
| Auditoria Completa | `make audit` |
| Sincronizar Tasks do GitHub | `make sync-tasks` |
| Limpar Caches | `make clean` |

---

*Documento de handoff cumulativo atualizado em 01/09/2026. Todo o conteúdo original de 31/08/2026 preservado integralmente, acrescido das entregas do dia 01/09/2026!* 🏎️🚀
