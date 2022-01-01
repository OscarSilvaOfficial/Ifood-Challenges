from typing import Optional
from app.infra.external.spotify import Spotify
from app.useCases.services.interfaces.userCases import UseCases

class TracksService(UseCases):
  
  def __init__(self, spotify=Spotify):
    self.spotify = Spotify()
    
  def get(self, id: Optional[int] = None):
    return self.spotify.get_music_tracks(id)
    
  def create(self, data):
    pass
    
  def update(self, id, data):
    pass
    
  def delete(self, id):
    pass