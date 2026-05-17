import requests

def test_ssrf_localhost():
    """
    Testa o endpoint /fetch_url para identificar possível vulnerabilidade SSRF permitindo acesso a localhost.
    Adapte a URL 'base_url' conforme o endpoint real da sua aplicação.
    """
    base_url = "http://localhost:5000/fetch_url"
    ssrf_target = "http://127.0.0.1:80"
    try:
        response = requests.get(f"{base_url}?url={ssrf_target}", timeout=5)
        assert response.status_code != 200, "Possível SSRF detectada: acesso ao localhost permitido!"
    except requests.exceptions.RequestException:
        pass  # Esperado em caso de proteção/no acesso ao endereço interno

def test_ssrf_cloud_metadata():
    """
    Testa o endpoint para acesso ao metadata service (comum em ambientes cloud).
    """
    base_url = "http://localhost:5000/fetch_url"
    cloud_url = "http://169.254.169.254/latest/meta-data/"
    try:
        response = requests.get(f"{base_url}?url={cloud_url}", timeout=5)
        assert response.status_code != 200, "Possível SSRF detectada: acesso ao metadata da nuvem permitido!"
    except requests.exceptions.RequestException:
        pass
