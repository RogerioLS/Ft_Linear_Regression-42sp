#!/bin/bash
# ==============================================================================
#      42 FT_LINEAR_REGRESSION — MASTER KANBAN & LABELS RUNNER
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🧙‍♂️ Iniciando automação do Kanban para 42 ft_linear_regression..."

# 1. Executar Etapa 1: Labels & Milestones
"$SCRIPT_DIR/01_setup_labels_and_milestones.sh"

echo ""

# 2. Executar Etapa 2: Tasks & Issues (Idempotente)
"$SCRIPT_DIR/02_setup_kanban_tasks.sh"

echo ""
echo "======================================================================"
echo " ✅ KANBAN 100% CONFIGURADO NO GITHUB!"
echo " 👉 Acesse a aba 'Issues' / 'Projects' no repositório para acompanhar."
echo "======================================================================"
