from app.core.interfaces.music_tracks import MusicTracksInterface


class MusicTracks(MusicTracksInterface):
  
  def __init__(self, degrees_celsius, music_tracks: MusicTracksInterface):
    self.degrees_celsius = degrees_celsius
  
  def get_tracks(self):
    pass