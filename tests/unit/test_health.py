from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_liveness():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "marketplace_reviews_processed_total" in response.text
