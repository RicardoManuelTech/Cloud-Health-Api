from app import app
import json

def test_health_endpoint():
  client = app.test_client()
  response = client.get("/health")
  assert response.status_code == 200
  data = json.loads(response.data)
  assert data["status"] == "healthy"


def test_version_endpoint():
    client = app.test_client()
    response = client.get("/version")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["version"] == "1.0.0"


def test_not_found_error():
    client = app.test_client()
    response = client.get("/does-not-exist")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Not Found"
    assert data["message"] == "The requested resource does not exist."


def test_internal_server_error():
    client = app.test_client()
    response = client.get("/error")

    assert response.status_code == 500

    data = response.get_json()

    assert data["error"] == "Internal Server Error"
    assert data["message"] == "An unexpected error occurred."

def test_readiness_endpoint():
    client = app.test_client()
    response = client.get("/ready")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "ready"
    assert data["application"] == "Cloud Health API"