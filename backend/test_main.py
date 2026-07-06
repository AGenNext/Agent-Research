from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_platform_overview():
    response = client.get("/api/platform")
    assert response.status_code == 200
    payload = response.json()
    assert payload["name"] == "Agent-Research Platform"
    assert "research-objective-intake" in payload["flows"]


def test_create_objective():
    response = client.post(
        "/api/objectives",
        json={"title": "Governed research loop", "question": "How do we preserve evidence?"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "proposed"
