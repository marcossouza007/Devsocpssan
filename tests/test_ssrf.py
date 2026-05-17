import os

import pytest
import requests


BASE_URL = os.getenv("SSRF_TEST_BASE_URL", "http://localhost:5000").rstrip("/")
FETCH_URL_ENDPOINT = f"{BASE_URL}/fetch_url"


def _attempt_ssrf(target_url: str) -> requests.Response:
    try:
        return requests.get(
            FETCH_URL_ENDPOINT,
            params={"url": target_url},
            timeout=5,
            allow_redirects=False,
        )
    except requests.RequestException as exc:
        pytest.skip(f"Endpoint de teste indisponível em {FETCH_URL_ENDPOINT}: {exc}")


def test_ssrf_to_localhost_is_blocked():
    response = _attempt_ssrf("http://127.0.0.1:80")
    assert response.status_code >= 400, "Possível SSRF: acesso interno localhost não foi bloqueado"


def test_ssrf_to_cloud_metadata_is_blocked():
    response = _attempt_ssrf("http://169.254.169.254/latest/meta-data/")
    assert response.status_code >= 400, "Possível SSRF: acesso ao metadata cloud não foi bloqueado"
