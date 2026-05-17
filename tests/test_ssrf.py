import os
from typing import List

import pytest
import requests


BASE_URL = os.getenv("SSRF_TEST_BASE_URL", "http://localhost:5000").rstrip("/")
FETCH_URL_ENDPOINT = f"{BASE_URL}/fetch_url"
LOCALHOST_SENSITIVE_CONTENT_INDICATORS = ["root:x:0:0:", "ssh-rsa"]
CLOUD_METADATA_SENSITIVE_INDICATORS = ["ami-id", "instance-id", "security-credentials", "local-ipv4"]


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


def _assert_no_sensitive_data(response: requests.Response, indicators: List[str], message: str) -> None:
    body = response.text.lower()
    for indicator in indicators:
        assert indicator.lower() not in body, message


def test_ssrf_to_localhost_is_blocked():
    response = _attempt_ssrf("http://127.0.0.1")
    assert response.status_code >= 400, "Possível SSRF: acesso interno localhost não foi bloqueado"
    _assert_no_sensitive_data(
        response,
        LOCALHOST_SENSITIVE_CONTENT_INDICATORS,
        "Possível SSRF: conteúdo sensível interno retornado para localhost",
    )


def test_ssrf_to_cloud_metadata_is_blocked():
    response = _attempt_ssrf("http://169.254.169.254/latest/meta-data/")
    assert response.status_code >= 400, "Possível SSRF: acesso ao metadata cloud não foi bloqueado"
    _assert_no_sensitive_data(
        response,
        CLOUD_METADATA_SENSITIVE_INDICATORS,
        "Possível SSRF: dados de metadata cloud retornados",
    )
