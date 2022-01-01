import requests, json, os
from app.infra.configs.enviroment import CLIENT_ID, CLIENT_SECRET, \
  DEBUG, SPOTFY_API_URL, SPOTFY_AUTH_URL, TOKEN

class Spotfy:
  
  def __init__(
    self, 
    url=SPOTFY_API_URL, 
    auth_url=SPOTFY_AUTH_URL, 
    client_id=CLIENT_ID, 
    secret=CLIENT_SECRET,
    token=TOKEN
  ):
    self._url = url
    self._auth_url = auth_url
    self._client_id = client_id
    self._secret = secret
    self._token = token
    
  def _mount_api_request(self, playlist_id: int):
    request = {
      'url': f"{self._url}/playlists/{playlist_id}",
      'headers': {
        "Authorization": f"Bearer {self._token}"
      } 
    }
    return requests.get(**request).json()
  
  def _get_local_data(self):
    file_dir = f"{os.getcwd()}/app/infra/external/fake_data/playlists.json"
    data = json.load(open(file_dir))
    return data
  
  def get_music_tracks(self, playlist_id: int):
    return self._get_local_data() if DEBUG else self._mount_api_request(playlist_id)
