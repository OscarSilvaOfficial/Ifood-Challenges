from abc import ABC, abstractmethod

class MusicTracksInterface(ABC):
  
  @abstractmethod
  def get_tracks(self):
    pass