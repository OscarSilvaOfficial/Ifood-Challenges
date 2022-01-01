from app.infra.external.spotify import Spotify

spotify = Spotify()

def test_track_external():
  tracks = spotify.get_music_tracks('4xKZLaPLh99LGKRjRlHxyX?si=83c968361f034f16')
  assert type(tracks) == dict
  
