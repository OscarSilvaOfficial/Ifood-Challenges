from app.infra.external.spotify import Spotify

spotify = Spotify()

def test_track_external():
  tracks = spotify.get_playlist_tracks()
  assert type(tracks) == list
  
