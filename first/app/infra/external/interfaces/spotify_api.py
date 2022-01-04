from abc import ABC, abstractmethod

class SpotifyAPI(ABC):

  @abstractmethod
  def get_playlist(self, playlist_id):
    pass
  
  @abstractmethod
  def get_playlist_tracks(self):
    pass