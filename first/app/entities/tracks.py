from app.entities.interfaces.tracks import TracksModel

class Playlist():
  
  def __init__(self, musics: list):
    self.musics = musics
    
  def _get_track_style(self, climate: int):
    if self.climate > 30:
      return 'party'
    if self.climate >= 15 and self.climate <= 30:
      return 'pop'
    if self.climate >= 10 and self.climate <= 14:
      return 'rock'
    return 'classic'
  
  def get_playlist(self, climate: int):
    music_list = []
    for music in self.musics:
      # if music['style'] == self._get_track_style(self.climate):
      music_list.append(music)
    return music_list
  