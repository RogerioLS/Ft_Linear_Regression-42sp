# ==============================================================================
#                 42 FT_LINEAR_REGRESSION MASTER MAKEFILE
# ==============================================================================

PYTHON := python3
DATASET := dataset/data.csv
THETAS := thetas.json

# ANSI Color Codes & Formatting
RESET   := \033[0m
BOLD    := \033[1m
DIM     := \033[2m
CYAN    := \033[36m
GREEN   := \033[32m
YELLOW  := \033[33m
RED     := \033[31m
MAGENTA := \033[35m
BLUE    := \033[34m
WHITE   := \033[97m

.PHONY: help install train predict plot precision test norm compile audit summary check pre-commit clean

help:
	@printf "$(CYAN)┌──────────────────────────────────────────────────────────────────────────────┐\n$(RESET)"
	@printf "$(CYAN)│$(RESET) $(BOLD)$(MAGENTA)                   42 FT_LINEAR_REGRESSION — COMMAND CENTER                 $(RESET) $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)├──────────────────────────────────────────────────────────────────────────────┤\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make help$(RESET)       $(DIM)─$(RESET) Show this interactive help menu                           $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make install$(RESET)    $(DIM)─$(RESET) Install dependencies in local virtualenv                  $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make train$(RESET)      $(DIM)─$(RESET) Train Linear Regression model and save thetas.json        $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make predict$(RESET)    $(DIM)─$(RESET) Run interactive price estimation CLI                      $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make plot$(RESET)       $(DIM)─$(RESET) Plot dataset points and fitted regression line (Bonus)    $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make precision$(RESET)  $(DIM)─$(RESET) Calculate R2, MSE, RMSE, and MAE metrics (Bonus)          $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make test$(RESET)       $(DIM)─$(RESET) Run all automated unit test suites                        $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make norm$(RESET)       $(DIM)─$(RESET) Run 42 Norm & AST Anti-Cheating Auditor (no polyfit)      $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make compile$(RESET)    $(DIM)─$(RESET) Compile Python 3.10 syntax across all project files       $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make audit$(RESET)      $(DIM)─$(RESET) Full audit: compile + norm + unit tests                   $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make summary$(RESET)    $(DIM)─$(RESET) Generate local audit report (summary.md)                  $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make check$(RESET)      $(DIM)─$(RESET) Pre-commit sanity check across all project files          $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make pre-commit$(RESET) $(DIM)─$(RESET) Install pre-commit tool and set up git hooks              $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make clean$(RESET)      $(DIM)─$(RESET) Remove temporary cache and prediction files               $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)├──────────────────────────────────────────────────────────────────────────────┤\n$(RESET)"
	@printf "$(CYAN)│$(RESET)           $(BOLD)$(WHITE)    🔥 Crafted with • by $(YELLOW)@RogerioLS$(WHITE) $(DIM)•$(RESET) $(BOLD)$(CYAN)42 São Paulo 🇧🇷$(RESET)              $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)└──────────────────────────────────────────────────────────────────────────────┘\n$(RESET)"

install:
	@printf "$(BOLD)$(BLUE)📦 [INSTALL] Installing project dependencies...$(RESET)\n"
	@$(PYTHON) -m pip install -e ".[dev]"
	@printf "$(GREEN)✔ Dependencies installed successfully!$(RESET)\n"

train:
	@printf "$(BOLD)$(MAGENTA)🧠 [MODEL] Training Linear Regression via Gradient Descent...$(RESET)\n"
	@$(PYTHON) train.py $(DATASET)

predict:
	@printf "$(BOLD)$(MAGENTA)🔮 [PREDICT] Launching interactive price estimator...$(RESET)\n"
	@$(PYTHON) predict.py

plot:
	@printf "$(BOLD)$(BLUE)📈 [VISUALIZATION] Plotting regression line and data points...$(RESET)\n"
	@$(PYTHON) plot.py $(DATASET)

precision:
	@printf "$(BOLD)$(BLUE)🎯 [METRICS] Evaluating model precision (R2, MSE, MAE)...$(RESET)\n"
	@$(PYTHON) scripts/evaluate_metrics.py $(DATASET) $(THETAS)

test:
	@printf "$(BOLD)$(BLUE)🚀 [TESTS] Running all unit test suites...$(RESET)\n"
	@$(PYTHON) -m unittest discover -s tests -p "test_*.py"

norm:
	@printf "$(BOLD)$(YELLOW)🛡️ [NORM] Running 42 Norm & AST Anti-Cheating Auditor...$(RESET)\n"
	@$(PYTHON) scripts/norm_check.py

compile:
	@printf "$(BOLD)$(MAGENTA)⚡ [COMPILE] Verifying Python 3.10 syntax compilation...$(RESET)\n"
	@$(PYTHON) -m py_compile $$(find src scripts tests -name "*.py" 2>/dev/null) $$(find . -maxdepth 1 -name "*.py")
	@printf "$(GREEN)✔ Syntax compilation successful!$(RESET)\n"

audit: compile norm test
	@printf "\n$(BOLD)$(GREEN)======================================================================$(RESET)\n"
	@printf "$(BOLD)$(GREEN)   ✅ FULL AUDIT COMPLETE: Code is compliant & ready for evaluation!   $(RESET)\n"
	@printf "$(BOLD)$(GREEN)======================================================================$(RESET)\n\n"

summary:
	@printf "$(BOLD)$(BLUE)📊 [SUMMARY] Generating local audit report (summary.md)...$(RESET)\n"
	@$(PYTHON) scripts/generate_summary.py

check:
	@printf "$(BOLD)$(YELLOW)🔍 [CHECK] Running full pre-commit validation across all files...$(RESET)\n"
	@$(PYTHON) scripts/norm_check.py
	@pre-commit run --all-files
	@printf "$(GREEN)✔ All pre-commit & norm checks passed! Ready for git commit.$(RESET)\n\n"

sync-tasks:
	@printf "$(BOLD)$(CYAN)🔄 [SYNC] Synchronizing GitHub issues to local task files...$(RESET)\n"
	@$(PYTHON) scripts/sync_tasks.py
	@printf "$(GREEN)✔ Tasks successfully synchronized!$(RESET)\n"



pre-commit:
	@if command -v pre-commit > /dev/null 2>&1; then \
		printf "$(GREEN)✔ pre-commit is already installed.$(RESET)\n"; \
	else \
		printf "$(YELLOW)⏳ Installing pre-commit via pip...$(RESET)\n"; \
		$(PYTHON) -m pip install pre-commit; \
	fi
	@./scripts/install-hooks.sh
	@printf "$(GREEN)✔ pre-commit setup completed successfully!$(RESET)\n"

clean:
	@printf "$(BOLD)$(RED)🧹 [CLEAN] Removing temporary cache and generated files...$(RESET)\n"
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type d -name ".ruff_cache" -exec rm -rf {} +
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "thetas.json" -delete
	@find . -type f -name "thetas.csv" -delete
	@find . -type f -name "summary.md" -delete
	@rm -rf artifacts/
	@printf "$(GREEN)✔ Clean completed successfully.$(RESET)\n\n"
