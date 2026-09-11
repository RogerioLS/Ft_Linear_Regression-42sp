<table width="100%" align="center">
  <tr>
    <td align="center">
      <h1>🛡️ Security Policy</h1>
      <p>
        <strong>42 ft_linear_regression</strong> • Secure engineering practices, threat defense, and responsible disclosure
      </p>
    </td>
  </tr>
</table>

<table width="100%">
  <tr>
    <td align="center">
      <h3>📋 Supported Versions</h3>
    </td>
  </tr>
  <tr>
    <td>
      <p>
        Only the active Python version defined by the 42 curriculum is officially supported for security updates, bug fixes, and exercise validation:
      </p>
      <table width="100%">
        <thead>
          <tr>
            <th align="left">Version</th>
            <th align="center">Supported</th>
            <th align="left">Context</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>Python 3.10.x</code></td>
            <td align="center">✅ Yes</td>
            <td>Official runtime target for all 42 Machine Learning specialization modules.</td>
          </tr>
          <tr>
            <td><code>Python &lt; 3.10</code></td>
            <td align="center">❌ No</td>
            <td>Unsupported due to missing modern type hinting union syntax and syntax dependencies.</td>
          </tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

<table width="100%">
  <tr>
    <td colspan="2" align="center">
      <h3>🔒 Security Best Practices & Automated Scanning</h3>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>1. Automated Secret Detection</h4>
      <p>
        <code>detect-secrets</code> executes locally via pre-commit hooks (<code>make check</code>) before every commit, preventing accidental leaks of private tokens, passwords, or API keys.
      </p>
      <h4>2. Static Security Analysis</h4>
      <p>
        Bandit AST security scanning runs in <code>make audit</code> to detect common Python vulnerabilities, unsafe deserialization patterns, and shell injection risks.
      </p>
      <h4>3. Safe File I/O & Parameter Validation</h4>
      <p>
        CLI arguments sanitize input dataset paths and mileage values. Parameters are serialized using strictly safe standard JSON (<code>thetas.json</code>), prohibiting insecure formats like <code>pickle</code> or <code>eval</code>.
      </p>
    </td>
    <td width="50%" valign="top">
      <h4>4. Dependency Vulnerability Management</h4>
      <p>
        Automated dependency audits scan external packages (<code>pip</code>) and GitHub Actions to ensure zero known CVE vulnerabilities across the supply chain.
      </p>
      <h4>5. Environment Isolation</h4>
      <p>
        All development and execution is isolated inside dedicated virtual environments (<code>venv</code> or <code>conda</code>). Analytical scripts never run with elevated (<code>root</code> / <code>sudo</code>) privileges.
      </p>
      <h4>6. Controlled Error Handling</h4>
      <p>
        Runtime exceptions are intercepted gracefully without leaking raw stack traces, proprietary paths, or host environment variables into public outputs.
      </p>
    </td>
  </tr>
</table>

<table width="100%">
  <tr>
    <td align="center">
      <h3>🚨 Reporting a Vulnerability</h3>
    </td>
  </tr>
  <tr>
    <td>
      <p>If you discover a security vulnerability or accidental credential exposure in this repository, please report it responsibly:</p>
      <ol>
        <li><strong>Do NOT open a public GitHub issue.</strong> Public issues disclose potential attack vectors before remediation.</li>
        <li>Submit a private security advisory directly on GitHub or contact the maintainer (<a href="https://github.com/RogerioLS">@RogerioLS</a>).</li>
        <li>Include detailed steps to reproduce the issue, along with relevant logs, payloads, or code snippets.</li>
      </ol>
      <p>We appreciate your effort in keeping this learning repository secure, reliable, and compliant with best engineering standards.</p>
    </td>
  </tr>
</table>

<a href="#"><img align='right' src='https://raw.githubusercontent.com/RogerioLS/RogerioLS/main/foto_little.png' width='55'></a>
