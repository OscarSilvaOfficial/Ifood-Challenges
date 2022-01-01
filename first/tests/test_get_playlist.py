from fastapi.testclient import TestClient
from app.infra import mount_app

client = TestClient(mount_app())
  
def test_get_playlist_with_all_params():
  params = {
    'city': 'São Paulo', 
    'lat': '-23.564', 
    'lon': '-46.653'
  }
  response = client.get('/api', params=params)
  assert response.status_code == 200
  
def test_get_playlist_with_no_city_params():
  params = {
    'lat': '-23.564', 
    'lon': '-46.653'
  }
  response = client.get('/api', params=params)
  assert response.status_code == 200
  
def test_get_playlist_with_no_city_and_lat_params():
  params = {
    'lon': '-46.653'
  }
  response = client.get('/api', params=params)
  assert response.status_code == 404
  
def test_get_playlist_with_no_lon_and_lat_params():
  params = {
    'city': 'São Paulo'
  }
  response = client.get('/api', params=params)
  assert response.status_code == 200