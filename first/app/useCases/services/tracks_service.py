from app.entities.tracks import Playlist
from app.infra.external.openweathermap import OpenWeatherMap
from app.useCases.services.interfaces.userCases import UseCases
from app.infra.external.interfaces.climate_api import ClimateAPI
from app.infra.external.interfaces.spotify_api import SpotifyAPI
from app.infra.external.spotify import Spotify
from typing import Optional

class TracksService(UseCases):
  
  def __init__(self, spotify: SpotifyAPI=Spotify(), climate_api: ClimateAPI=OpenWeatherMap()):
    self.spotify = spotify
    self.climate_api = climate_api
  
  def get(self, city: Optional[str]=None, lat: Optional[str]=None, lon: Optional[str]=None):
    climate_temperature = self.climate_api.get_city_temperature(city, lat, lon)
    playlist = self.spotify.get_playlist_tracks()
    response_playlist = Playlist(musics=playlist)
    return response_playlist.get_playlist(climate=climate_temperature)
  