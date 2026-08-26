#!/bin/bash
# ==============================================================================
#      42 FT_LINEAR_REGRESSION — STEP 1: SETUP LABELS & MILESTONES
# ==============================================================================

set -e

REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)

if [ -z "$REPO" ]; then
    echo "❌ Erro: Não foi possível detectar o repositório GitHub via gh cli."
    echo "💡 Certifique-se de estar autenticado com 'gh auth login'."
    exit 1
fi

echo "🚀 [ETAPA 1] Configurando Milestones e Labels no repositório: $REPO..."

# ------------------------------------------------------------------------------
# 1. CRIAR MILESTONES
# ------------------------------------------------------------------------------
echo "🎯 Criando Milestones..."

gh api repos/$REPO/milestones -f title="01. Mathematical Foundations & Preprocessing" \
  -f description="Leitura de dados, normalização de features e implementação das fórmulas de hipótese e gradiente." 2>/dev/null || true

gh api repos/$REPO/milestones -f title="02. Training & Interactive Prediction Engine" \
  -f description="Implementação dos executáveis train.py e predict.py com persistência e desnormalização de pesos." 2>/dev/null || true

gh api repos/$REPO/milestones -f title="03. Bonuses, Visualization & Peer Defense" \
  -f description="Plot da reta de regressão e pontos (plot.py), cálculo de R2/MSE e preparação para avaliação presencial." 2>/dev/null || true

# ------------------------------------------------------------------------------
# 2. CRIAR LABELS
# ------------------------------------------------------------------------------
echo "🏷️ Criando Labels completas..."

# Labels de Áreas
gh label create "area: model" --color "e67e22" --description "Algoritmo de Regressão Linear e Gradiente" --force
gh label create "area: preprocessing" --color "1abc9c" --description "Feature scaling e normalização" --force
gh label create "area: visualization" --color "9b59b6" --description "Plotagem de gráficos e curvas de custo" --force
gh label create "area: defense" --color "2ecc71" --description "Preparação para avaliação presencial 42" --force
gh label create "area: devops" --color "34495e" --description "CI/CD, Makefiles, Linters e automação" --force

# Labels de Tipos
gh label create "type: implementation" --color "27ae60" --description "Desenvolvimento de código" --force
gh label create "type: math-heavy" --color "e74c3c" --description "Foco em Cálculo e Derivadas Parciais" --force
gh label create "type: pedagogical" --color "f1c40f" --description "Conceitos fundamentais explicados para estudo em dupla" --force
gh label create "type: defense" --color "16a085" --description "Foco em critérios de avaliação da 42" --force
gh label create "type: bonus" --color "95a5a6" --description "Funcionalidades bônus obrigatórias da entrega" --force
gh label create "type: test" --color "d35400" --description "Testes unitários e suites de validação" --force
gh label create "type: docs" --color "7f8c8d" --description "Documentação técnica e científica" --force

# Labels de Prioridade
gh label create "priority: high" --color "b91c1c" --description "Prioridade Alta / Bloqueante" --force
gh label create "priority: medium" --color "f59e0b" --description "Prioridade Média" --force
gh label create "priority: low" --color "10b981" --description "Prioridade Baixa / Melhoria" --force

echo "✅ Milestones e Labels configuradas com sucesso!"
