#!/bin/bash
# ==============================================================================
#      42 FT_LINEAR_REGRESSION — STEP 2: SETUP KANBAN TASKS (IDEMPOTENT)
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ISSUES_DIR="$SCRIPT_DIR/../issues"

REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)

if [ -z "$REPO" ]; then
    echo "❌ Erro: Não foi possível detectar o repositório GitHub via gh cli."
    exit 1
fi

echo "🚀 [ETAPA 2] Populando o Kanban com as tasks no repositório: $REPO..."

create_issue_if_missing() {
    local title="$1"
    local milestone="$2"
    local labels="$3"
    local body_file="$4"

    local existing=$(gh issue list --search "$title in:title" --json number -q '.[0].number' 2>/dev/null || true)

    if [ -n "$existing" ]; then
        echo "🔄 Atualizando corpo da Issue existente (#$existing): $title"
        gh issue edit "$existing" \
            --milestone "$milestone" \
            --add-label "$labels" \
            --body-file "$body_file"
    else
        echo "➕ Criando issue: $title"
        gh issue create \
            --title "$title" \
            --milestone "$milestone" \
            --label "$labels" \
            --body-file "$body_file"
    fi
}

# --- MILESTONE 1: Mathematical Foundations & Preprocessing ---

create_issue_if_missing \
  "[LR-01] Data Pipeline: Leitura de CSV e Normalização Min-Max" \
  "01. Mathematical Foundations & Preprocessing" \
  "area: preprocessing,type: implementation,type: pedagogical,priority: high" \
  "$ISSUES_DIR/lr-01-data-pipeline.md"

create_issue_if_missing \
  "[LR-02] Core Math: Hipótese, Custo MSE e Derivadas Parciais do Gradiente" \
  "01. Mathematical Foundations & Preprocessing" \
  "area: model,type: math-heavy,type: implementation,priority: high" \
  "$ISSUES_DIR/lr-02-core-math-gradient.md"

create_issue_if_missing \
  "[LR-03] Test Suite: Validação Unitária do Gradiente e Convergência" \
  "01. Mathematical Foundations & Preprocessing" \
  "area: model,type: test,type: implementation,priority: high" \
  "$ISSUES_DIR/lr-03-test-suite.md"

# --- MILESTONE 2: Training & Interactive Prediction Engine ---

create_issue_if_missing \
  "[LR-04] CLI train.py: Treinamento e Persistência de Thetas" \
  "02. Training & Interactive Prediction Engine" \
  "area: model,type: implementation,priority: high" \
  "$ISSUES_DIR/lr-04-cli-train.md"

create_issue_if_missing \
  "[LR-05] CLI predict.py: Predição Interativa no Terminal com Fallback" \
  "02. Training & Interactive Prediction Engine" \
  "area: model,type: implementation,priority: high" \
  "$ISSUES_DIR/lr-05-cli-predict.md"

create_issue_if_missing \
  "[LR-06] Desnormalização Analítica: Thetas no Espaço Real" \
  "02. Training & Interactive Prediction Engine" \
  "area: preprocessing,type: math-heavy,type: implementation,priority: high" \
  "$ISSUES_DIR/lr-06-denormalization-unscaling.md"

# --- MILESTONE 3: Bonuses, Visualization & Peer Defense ---

create_issue_if_missing \
  "[LR-07] Bonus: CLI plot.py (Dispersão + Reta de Regressão + Curva de Custo)" \
  "03. Bonuses, Visualization & Peer Defense" \
  "area: visualization,type: bonus,type: implementation,priority: high" \
  "$ISSUES_DIR/lr-07-bonus-cli-plot.md"

create_issue_if_missing \
  "[LR-08] Bonus: Métricas de Precisão (R2, MSE, MAE) e Roteiro de Peer Defense" \
  "03. Bonuses, Visualization & Peer Defense" \
  "area: defense,type: bonus,type: defense,priority: high" \
  "$ISSUES_DIR/lr-08-bonus-precision-defense.md"

echo "🎉 Todas as Tasks de ft_linear_regression foram configuradas com sucesso!"
