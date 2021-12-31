from fastapi.testclient import TestClient
from app.infra import mount_app

client = TestClient(mount_app())
  
def test_get_index_message():
  response = client.get('/')
  print(response.json())
  assert response.status_code == 200