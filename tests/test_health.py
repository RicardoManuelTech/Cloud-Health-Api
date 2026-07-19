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
