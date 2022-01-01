from app.infra.external.spotfy import Spotfy

spotfy = Spotfy()

def test_track_external():
  tracks = spotfy.get_music_tracks('4xKZLaPLh99LGKRjRlHxyX?si=83c968361f034f16')
  print (type(tracks))
  
