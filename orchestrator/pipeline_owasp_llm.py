import subprocess
import openai
from datetime import datetime
import os
import json

# 1. Checklist de Segurança (automatizado usando LLM)
def get_security_checklist_llm():
    prompt = (
        "Gere um checklist OWASP atualizado para revisar segurança em aplicações, APIs, sistemas e cloud. Liste os principais itens para garantir conformidade com padrões modernos de segurança."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use o modelo que preferir/configurado
        messages=[{"role": "user", "content": prompt}]
    )
    checklist = response['choices'][0]['message']['content']
    print("Checklist de Segurança OWASP LLM:\n")
    print(checklist)
    with open("owasp_checklist.txt", "w", encoding="utf-8") as f:
        f.write(checklist)

# 2. Scanner LLM automático (Exemplo com OWASP LLM Scanner CLI)
def run_owasp_llm_scanner(target_dir='.', output_file='llm_report.json'):
    print(f'Executando scanner LLM OWASP em "{target_dir}"...')
    # Exemplo: ajuste o comando conforme seu ambiente/CLI/versão
    try:
        subprocess.run([
            "python3", "-m", "llmscanner", "--target", target_dir, "--output", output_file, "--format", "json"
        ], check=True)
        print(f"Relatório JSON gerado: {output_file}")
    except Exception as e:
        print("Erro ao rodar o scanner LLM:", e)

# 3. Gerar relatório amigável
def generate_html_report(json_file='llm_report.json', html_file='owasp_llm_report.html'):
    if not os.path.exists(json_file):
        print("Relatório JSON não encontrado. Pulei a etapa HTML.")
        return
    with open(json_file, encoding="utf-8") as f:
        data = json.load(f)
    html = f"<h2>Relatório de Vulnerabilidades — LLM OWASP<br><small>{datetime.now().strftime('%Y-%m-%d %H:%M')}</small></h2>\n"
    html += "<ul>\n"
    for vuln in data.get("vulnerabilities", []):
        html += (
            f"<li><strong>{vuln.get('title','')}</strong>: {vuln.get('description','')}"
            f" <i>({vuln.get('location','local não informado')})</i></li>\n"
        )
    html += "</ul>\n"
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Relatório HTML salvo em: {html_file}")

if __name__ == "__main__":
    # 1. Checklist de segurança por LLM
    get_security_checklist_llm()
    # 2. Scanner de vulnerabilidades usando OWASP LLM (ajuste caminho se necessário)
    run_owasp_llm_scanner(target_dir='.', output_file='llm_report.json')
    # 3. Relatório para visualização amigável
    generate_html_report(json_file='llm_report.json', html_file='owasp_llm_report.html')
    print("\nPipeline de segurança OWASP LLM concluído!\nRelatórios gerados: owasp_checklist.txt  |  owasp_llm_report.html\n")
