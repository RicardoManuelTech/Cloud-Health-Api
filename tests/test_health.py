from app import app
import json

def test_health_endpoint():
  client = app.test_client()
  response = client.get("/health")
  assert response.status_code == 200
  data = json.loads(response.data)
  assert data["status"] == "healthy"
