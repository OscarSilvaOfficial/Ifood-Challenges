from app.entities.interfaces.tracks import TracksModel

class Playlist(TracksModel):
  
  def __init__(self, musics: list):
    self._musics = musics
    
  def _get_track_style(self, climate: int):
    if climate > 30:
      return 'party'
    if climate >= 15 and climate <= 30:
      return 'pop'
    if climate >= 10 and climate <= 14:
      return 'rock'
    return 'classic'
    
  def musics(self, climate: int):
    music_list = []
    for music in self._musics:
      if music['style'] == self._get_track_style(climate):
        music_list.append(music)
    return music_list
  