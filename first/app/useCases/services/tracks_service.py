from typing import Optional
from app.infra.external.spotify import Spotify
from app.useCases.services.interfaces.userCases import UseCases

class TracksService(UseCases):
  
  def __init__(self, spotify=Spotify):
    self.spotify = Spotify()
    
  """
  Descobrir a temperatura da cideda, e com base nisso retornar uma lista de musicas
  """ 
  def get(self, city: Optional[str]=None, lat: Optional[str]=None, lon: Optional[str]=None):
    return self.spotify.get_playlist_tracks()
  