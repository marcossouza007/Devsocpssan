import subprocess

class SAST:
    def run_gitleaks(self, target="."):
        return subprocess.run(['gitleaks', 'detect', '-s', target, '--report-path', 'gitleaks.json'], capture_output=True)
    def run_semgrep(self, target="."):
        return subprocess.run(['semgrep', '--config', 'p/owasp-top-ten', target, '--json'], capture_output=True)
    def run_sonarqube(self):
        # Exemplo: Substitua com integração real SonarQube CLI/API
        return "sonarqube result mock"

class DAST:
    def run_zap(self, target_url):
        # OWASP ZAP CLI: zap-cli/python-zapv2 API
        # Exemplo mínimo
        return subprocess.run(['zap-cli', 'quick-scan', '-r', target_url], capture_output=True)
    def run_nuclei(self, target_url):
        return subprocess.run(['nuclei', '-target', target_url, '-json'], capture_output=True)
