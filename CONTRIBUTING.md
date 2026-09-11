<table width="100%" align="center">
  <tr>
    <td align="center">
      <h1>🚀 Contributing Guidelines</h1>
      <p>
        <strong>42 ft_linear_regression</strong> • Engineering protocols, quality gates, mathematical standards, and git governance
      </p>
    </td>
  </tr>
</table>

<table width="100%">
  <tr>
    <td align="center">
      <h3>🛠️ Centralized Command Center (Makefile)</h3>
    </td>
  </tr>
  <tr>
    <td>
      <p>
        All development, linting, testing, and lifecycle tasks are standardized through the interactive <strong>Makefile</strong>. Always prefer using <code>make</code> targets rather than manual python commands:
      </p>
      <table width="100%">
        <thead>
          <tr>
            <th align="left">Command</th>
            <th align="left">Purpose</th>
            <th align="left">When to Use</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>make help</code></td>
            <td>Displays the interactive command menu with descriptions</td>
            <td>Anytime you need a quick command refresher</td>
          </tr>
          <tr>
            <td><code>make onboarding</code></td>
            <td>Displays architecture overview and guidelines banner</td>
            <td>Welcoming new contributors to the repository</td>
          </tr>
          <tr>
            <td><code>make install</code></td>
            <td>Installs dependencies in editable mode and configures git hooks</td>
            <td>First-time project setup or environment recreation</td>
          </tr>
          <tr>
            <td><code>make check</code></td>
            <td>Runs pre-commit linters, code formatters, and AST norm checks</td>
            <td><strong>Mandatory before staging files or committing</strong></td>
          </tr>
          <tr>
            <td><code>make norm</code></td>
            <td>Audits docstrings, <code>__main__</code> guards, and anti-cheating rules</td>
            <td>To verify strict 42 norm compliance</td>
          </tr>
          <tr>
            <td><code>make compile</code></td>
            <td>Verifies Python 3.10 syntax compilation across all files</td>
            <td>Fast syntax validation</td>
          </tr>
          <tr>
            <td><code>make test</code></td>
            <td>Executes unit and integration test suites recursively</td>
            <td>After any algorithmic or pipeline modification</td>
          </tr>
          <tr>
            <td><code>make audit</code></td>
            <td>Runs complete verification suite (<code>compile</code> + <code>norm</code> + <code>test</code>)</td>
            <td>Before pushing or opening a Pull Request</td>
          </tr>
          <tr>
            <td><code>make summary</code></td>
            <td>Generates local Markdown audit report (<code>summary.md</code>)</td>
            <td>To preview the PR audit comment locally</td>
          </tr>
          <tr>
            <td><code>make sync-tasks</code></td>
            <td>Synchronizes remote GitHub issues to <code>.github/issues/</code></td>
            <td>To recognize new project tasks offline in git hooks</td>
          </tr>
          <tr>
            <td><code>make train</code></td>
            <td>Trains Linear Regression via Gradient Descent & saves thetas</td>
            <td>Milestone 2 model training execution</td>
          </tr>
          <tr>
            <td><code>make predict</code></td>
            <td>Runs interactive / CLI mileage prediction with <code>thetas.json</code></td>
            <td>Milestone 2 inference verification</td>
          </tr>
          <tr>
            <td><code>make plot</code></td>
            <td>Displays scatter plot, regression line, and loss decay</td>
            <td>Milestone 3 visual evaluation</td>
          </tr>
          <tr>
            <td><code>make evaluate</code></td>
            <td>Computes $R^2$, MSE, RMSE, and MAE precision bonus metrics</td>
            <td>Milestone 3 bonus verification</td>
          </tr>
          <tr>
            <td><code>make clean</code></td>
            <td>Removes temporary cache files (<code>__pycache__</code>, <code>.pyc</code>)</td>
            <td>Workspace hygiene</td>
          </tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

<table width="100%">
  <tr>
    <td colspan="2" align="center">
      <h3>🏷️ Branch, Commit & Task Naming Governance</h3>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🌿 1. Branch Naming Format</h4>
      <pre><code>&lt;type&gt;/&lt;task-id&gt;-&lt;short-description-in-kebab-case&gt;</code></pre>
      <ul>
        <li><code>feat/lr-01-data-pipeline</code></li>
        <li><code>feat/lr-02-core-math-gradient</code></li>
        <li><code>fix/lr-04-learning-rate-divergence</code></li>
        <li><code>chore/infra-align-dslr-architecture</code></li>
      </ul>
      <p>
        <em>Note: If a branch is improperly named, the <code>branch_lint.yml</code> CI workflow will automatically comment instructions and close the PR.</em>
      </p>
    </td>
    <td width="50%" valign="top">
      <h4>📝 2. Commit Message Format</h4>
      <pre><code>&lt;type&gt;(&lt;scope&gt;): [&lt;TASK-ID&gt;] &lt;short description in lowercase&gt;</code></pre>
      <ul>
        <li><code>feat(preprocessing): [LR-01:#1] implement minmax scaler from scratch</code></li>
        <li><code>feat(model): [LR-02:#2] implement gradient descent batch training</code></li>
        <li><code>chore(infra): [INFRA] configure pre-commit hooks and make check</code></li>
      </ul>
      <p>
        <strong>Allowed Reserved Tags (non-subject):</strong><br>
        <code>[INFRA]</code>, <code>[CHORE]</code>, <code>[DOCS]</code>, <code>[FIX]</code>, <code>[HOTFIX]</code>, <code>[SECURITY]</code>, <code>[RELEASE]</code>, <code>[CONFIG]</code>, <code>[DEPS]</code>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <h4>🔄 Dynamic Task Lifecycle & Troubleshooting</h4>
      <ul>
        <li><strong>Dynamic Detection:</strong> Git hooks in <code>.githooks/commit-msg</code> scan <code>.github/issues/</code> to validate task IDs dynamically without hardcoding.</li>
        <li><strong>If your commit is rejected:</strong> Run <code>make sync-tasks</code> to refresh offline issues, or use an allowed tag (e.g. <code>[INFRA]</code>) if not tied to a Kanban task.</li>
        <li><strong>If your PR is rejected by CI:</strong> Rename your branch locally with <code>git branch -m &lt;new-name&gt;</code>, push upstream with <code>git push -u origin &lt;new-name&gt;</code>, and delete the old branch on origin.</li>
      </ul>
    </td>
  </tr>
</table>

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🧪 Testing Pyramid Architecture</h3>
      <p>All automated tests are maintained under the <code>tests/</code> tree:</p>
      <ul>
        <li>
          <strong><code>tests/unit/</code>:</strong>
          Validates atomic math functions in isolation (<code>src/preprocessing/scaler.py</code>, <code>src/model/linear_regression.py</code>) against manual chalk-board derivations.
        </li>
        <li>
          <strong><code>tests/integration/</code>:</strong>
          Tests end-to-end CLI workflows and pipeline behavior (<code>train.py</code>, <code>predict.py</code>, <code>plot.py</code>).
        </li>
      </ul>
      <p>Run test execution suite: <code>make test</code></p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🛡️ 42 Norm & Academic Integrity</h3>
      <ul>
        <li><strong>Python 3.10+:</strong> Strictly use standard library, NumPy, and Matplotlib.</li>
        <li><strong>Line Length:</strong> Strict limit of <strong>100 characters per line</strong>.</li>
        <li><strong>Docstrings:</strong> Mandatory for every module, class, and method.</li>
        <li><strong>Execution Guards:</strong> Scripts must include <code>if __name__ == "__main__":</code>.</li>
        <li><strong>Zero Black-Box Solvers:</strong> Prohibits <code>sklearn.linear_model</code>, <code>np.polyfit</code>, <code>scipy.optimize</code>. All gradients and updates must be derived by hand.</li>
      </ul>
    </td>
  </tr>
</table>

<table width="100%">
  <tr>
    <td align="center">
      <h3>🚀 Pre-Push Quality Gate Checklist</h3>
    </td>
  </tr>
  <tr>
    <td>
      <p>Before pushing your branch or requesting peer review, guarantee that:</p>
      <ol>
        <li><code>make check</code> passes 100% with zero linter, formatter, or security warnings;</li>
        <li><code>make audit</code> passes with all unit tests green and zero 42 norm violations;</li>
        <li>Your branch and commits follow the semantic naming convention;</li>
        <li><code>CHANGELOG.md</code> is updated with your contributions under the <code>[Unreleased]</code> section.</li>
      </ol>
    </td>
  </tr>
</table>

<a href="#"><img align='right' src='https://raw.githubusercontent.com/RogerioLS/RogerioLS/main/foto_little.png' width='55'></a>
