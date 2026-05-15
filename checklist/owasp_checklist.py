OWASP_TOP_10 = [
    "A01 - Broken Access Control",
    "A02 - Cryptographic Failures",
    "A03 - Injection",
    "A04 - Insecure Design",
    "A05 - Security Misconfiguration",
    "A06 - Vulnerable and Outdated Components",
    "A07 - Identification and Authentication Failures",
    "A08 - Software and Data Integrity Failures",
    "A09 - Security Logging and Monitoring Failures",
    "A10 - Server-Side Request Forgery (SSRF)"
]

class Checklist:
    def __init__(self):
        self.results = {k: {"found": [], "missing": []} for k in OWASP_TOP_10}
    
    def triage(self, sast_report, dast_report):
        for item in OWASP_TOP_10:
            # Busca pelo nome da falha nos relatórios e preenche os resultados
            if item in sast_report or item in dast_report:
                self.results[item]["found"].append("Evidências encontradas no relatório.")
            else:
                self.results[item]["missing"].append("Cobertura ausente ou não identificada.")
        return self.results

    def report(self):
        # Consolidação simples de resultados
        return self.results
