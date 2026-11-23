import httpx


def test_readyz(base_url: str) -> None:
    response = httpx.get(f"{base_url}/readyz", timeout=5, trust_env=False)
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
