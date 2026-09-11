<table width="100%">
  <tr></tr>
  <tr>
    <td colspan="2" align="center">
      <h1>🚗 42 FT_LINEAR_REGRESSION</h1>
      <h3>Car Price Prediction from Scratch via Batch Gradient Descent</h3>
      <p align="center">
        <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python&logoColor=white" alt="Python 3.10+"/>
        <img src="https://img.shields.io/badge/Norm_42-100%25_Compliant-2ea44f?style=flat&logo=checkmarx&logoColor=white" alt="Norm 42"/>
        <img src="https://img.shields.io/badge/Anti--Cheating-AST_Audited-8957e5?style=flat&logo=shield&logoColor=white" alt="Anti Cheating"/>
        <img src="https://img.shields.io/badge/Target_Precision-R%C2%B2_%E2%89%A5_73%25-success?style=flat" alt="Precision"/>
        <img src="https://img.shields.io/badge/License-MIT-purple?style=flat" alt="License"/>
      </p>
      <p align="center">
        <a href="https://rogeriols.github.io/Ft_Linear_Regression-42sp/" target="_blank">
          <img src="https://img.shields.io/badge/Interactive_Journey-GitHub_Pages-0969da?style=flat&logo=githubpages&logoColor=white" alt="GitHub Pages Masterclass"/>
        </a>
        <a href="https://github.com/RogerioLS/Ft_Linear_Regression-42sp/actions/workflows/audit.yml" target="_blank">
          <img src="https://github.com/RogerioLS/Ft_Linear_Regression-42sp/actions/workflows/audit.yml/badge.svg" alt="Audit Quality Gate"/>
        </a>
        <img src="https://img.shields.io/badge/%C3%89cole_42-S%C3%A3o_Paulo_🇧🇷-000000?style=flat&logo=42&logoColor=white" alt="42 SP"/>
      </p>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td width="55%">
      <p>
        🎯 <strong>Mission & Objective:</strong><br>
        Implementation of a univariate <strong>Linear Regression model from raw mathematical first principles</strong> to predict used car prices from mileage (<code>km</code> $\to$ <code>price</code>).
      </p>
      <p>
        🛡️ <strong>Zero-Cheating Architecture:</strong><br>
        Strictly zero usage of black-box ML solvers (<code>np.polyfit</code>, <code>sklearn.linear_model</code>, <code>scipy.optimize</code>). All gradients, loss surfaces, and parameter update steps are derived analytically and coded by hand.
      </p>
      <p>
        ⚡ <strong>Numerical Stability & Feature Scaling:</strong><br>
        Addresses numerical gradient explosion caused by large kilometer magnitudes ($240,000\text{ km}$) via handcrafted Min-Max normalization $[0.0, 1.0]$ coupled with closed-form analytical parameter de-normalization.
      </p>
      <p>
        🌐 <strong>Interactive Masterclass:</strong><br>
        Includes an interactive educational journey deployed to <strong>GitHub Pages</strong> with live gradient simulation, step-by-step trace tables, and cost decay visualizers.
      </p>
    </td>
    <td width="45%" align="center">
      <img src="docs/assets/training_animation.gif" alt="Gradient Descent Convergence Simulation" width="100%" style="border-radius: 6px;"/>
      <p align="center">
        <sub><em>Live Batch Gradient Descent Convergence (Actual Dataset)</em></sub>
      </p>
    </td>
  </tr>
</table>

<table width="100%" align="center">
  <tr></tr>
  <tr>
    <td colspan="3" align="center">
      <h3>📐 Mathematical Formulation & First Principles</h3>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td width="25%"><strong>Concept</strong></td>
    <td width="40%"><strong>Mathematical Formulation</strong></td>
    <td width="35%"><strong>Computational Implementation</strong></td>
  </tr>
  <tr></tr>
  <tr>
    <td><strong>Linear Hypothesis</strong></td>
    <td>$$h_\theta(x) = \theta_0 + (\theta_1 \cdot x)$$</td>
    <td>Vectorized evaluation: <code>self.theta0 + (self.theta1 * arr_x)</code></td>
  </tr>
  <tr></tr>
  <tr>
    <td><strong>Cost Function (MSE Loss)</strong></td>
    <td>$$J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})^2$$</td>
    <td>Calculates half Mean Squared Error across all training observations.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><strong>Analytical Gradients</strong></td>
    <td>
      $$\frac{\partial J}{\partial \theta_0} = \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)})$$<br>
      $$\frac{\partial J}{\partial \theta_1} = \frac{1}{m} \sum_{i=0}^{m-1} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$$
    </td>
    <td>Simultaneous exact partial derivatives computed with zero numerical approximation.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><strong>Simultaneous Parameter Updates</strong></td>
    <td>
      $$\text{tmp}_0 = \theta_0 - \alpha \frac{\partial J}{\partial \theta_0}$$<br>
      $$\text{tmp}_1 = \theta_1 - \alpha \frac{\partial J}{\partial \theta_1}$$
    </td>
    <td>Synchronous parameter update via temporary buffers preventing gradient leakage.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><strong>Parameter Unscaling</strong></td>
    <td>
      $$\theta_1^{real} = \theta_1^{norm} \cdot \left(\frac{y_{max} - y_{min}}{x_{max} - x_{min}}\right)$$<br>
      $$\theta_0^{real} = y_{min} + \theta_0^{norm} \Delta y - \theta_1^{real} x_{min}$$
    </td>
    <td>Analytical transformation mapping scaled weights back to physical real-world units ($/km).</td>
  </tr>
</table>

<table width="100%">
  <tr></tr>
  <tr>
    <td colspan="3" align="center">
      <h3>📦 42 Deliverables Contract & Executables</h3>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td width="20%"><strong>Executable</strong></td>
    <td width="15%"><strong>Category</strong></td>
    <td width="25%"><strong>Terminal Command</strong></td>
    <td width="40%"><strong>Scope & Expected Output</strong></td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>train.py</code></td>
    <td><span style="color: #2ea44f;">Mandatory</span></td>
    <td><code>make train</code></td>
    <td>Lê <code>dataset/data.csv</code>, treina o modelo via Batch Gradient Descent e exporta <code>thetas.json</code>.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>predict.py</code></td>
    <td><span style="color: #2ea44f;">Mandatory</span></td>
    <td><code>make predict</code></td>
    <td>Prompt interativo para estimativa de preço por quilometragem com fallback para $\theta=0$.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>plot.py</code></td>
    <td><span style="color: #8957e5;">Bonus</span></td>
    <td><code>make plot</code></td>
    <td>Renderiza dispersão de dados, reta de regressão ajustada e curva de custo $J(\theta)$ ao longo das épocas.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>evaluate_metrics.py</code></td>
    <td><span style="color: #8957e5;">Bonus</span></td>
    <td><code>make precision</code></td>
    <td>Avalia métricas estatísticas: Coeficiente de Determinação ($R^2 \ge 0.73$), $MSE$, $RMSE$ e $MAE$.</td>
  </tr>
</table>

<table width="100%">
  <tr></tr>
  <tr>
    <td colspan="3" align="center">
      <h3>🕹️ Command Center & Quality Gates (Makefile)</h3>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td width="25%"><strong>Target</strong></td>
    <td width="25%"><strong>Category</strong></td>
    <td width="50%"><strong>Action & Quality Check</strong></td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>make onboarding</code></td>
    <td>Developer Experience</td>
    <td>Exibe guia de boas práticas, padrões de branch, formato de commits e regras institucionais.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>make install</code></td>
    <td>Setup & Tooling</td>
    <td>Instala dependências do projeto em modo editável e configura os git hooks em <code>.githooks/</code>.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>make audit</code></td>
    <td>Quality Gate 42</td>
    <td>Valida compilação Python 3.10, auditor AST Anti-Cheating e executa 100% da suíte de testes unitários.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>make check</code></td>
    <td>Sanity Check</td>
    <td>Executa bateria de linters pré-commit: Black, isort, flake8, ruff e scanner de secrets.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>make test</code></td>
    <td>Automated Tests</td>
    <td>Roda suíte completa de testes unitários e de integração (21+ testes automatizados).</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>make clean</code></td>
    <td>Maintenance</td>
    <td>Remove caches temporários (<code>__pycache__</code>, <code>.pytest_cache</code>, <code>thetas.json</code>, <code>summary.md</code>).</td>
  </tr>
</table>

<table width="100%">
  <tr></tr>
  <tr>
    <td colspan="2" align="center">
      <h3>🏛️ Repository Architecture & Engineering Modules</h3>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td width="35%"><strong>Module / Directory</strong></td>
    <td width="65%"><strong>Architectural Responsibility</strong></td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>src/model/</code></td>
    <td>Núcleo de Regressão Linear: cálculo analítico de gradientes, função de custo MSE e Batch Gradient Descent.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>src/preprocessing/</code></td>
    <td>Pipeline de dados: carregador de CSV e normalizador Min-Max com desnormalização paramétrica analítica.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>src/visualization/</code></td>
    <td>Módulo de plotagem gráfica: dispersão de pontos, reta ajustada e convergência da curva de perda.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>tests/unit/</code></td>
    <td>Pirâmide de testes unitários com validação contra valores exatos da lousa didática e decaimento monotônico.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>scripts/</code></td>
    <td>Auditor AST Anti-Cheating, Milestone Release Bot, linters de governança de branch/commit e avaliador de métricas.</td>
  </tr>
  <tr></tr>
  <tr>
    <td><code>.github/workflows/</code></td>
    <td>Pipelines CI/CD: Quality Gate rigoroso, auto-fechamento de PRs fora do padrão e deploy no GitHub Pages.</td>
  </tr>
</table>

<a href="#"><img align='right' src='https://raw.githubusercontent.com/RogerioLS/RogerioLS/main/foto_little.png' width='55'></a>
