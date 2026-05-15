# DevSecOps Pentest Automation

Este projeto automatiza a análise de segurança contínua com integração DevSecOps baseada no OWASP Top 10, usando ferramentas livres e módulos em Python (SAST, DAST e orquestração de relatórios).

**Ferramentas integráveis:** Gitleaks, Semgrep, SonarQube, ZAP, Nuclei, DefectDojo.

## Como rodar

- Tenha Python 3.8+ e as ferramentas de segurança instaladas (Gitleaks, Semgrep, etc).
- Instale dependências:  
  `pip install -r requirements.txt`
- Execute scripts conforme necessidade ou configure direto no pipeline CI/CD.

## Pipeline GitHub Actions

Veja o exemplo em `.github/workflows/security.yml`.
