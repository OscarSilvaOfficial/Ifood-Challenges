from app.entities.interfaces.tracks import TracksModel

class Tracks(TracksModel):
  
  def __init__(self, musics: list):
    self._musics = musics
    
  @property
  def musics(self):
    return self._musics