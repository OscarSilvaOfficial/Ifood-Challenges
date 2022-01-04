import requests
from app.infra.configs.enviroment import OPENWEATHERMAP_SECRET, OPENWEATHERMAP_URL

class OpenWeatherMap:
  
  def __init__(
    self, 
    url=OPENWEATHERMAP_URL,
    secret=OPENWEATHERMAP_SECRET
  ):
    self._url = url
    self._secret = secret
    self._metrics = 'units=metric'
    
  def _get_city_info(self, city=None, lat=None, lon=None):
    if not city:
      return requests.get(f'{self._url}?lat={lat}&lon={lon}&appid={self._secret}&{self._metrics}')
    return requests.get(f'{self._url}?q={city}&appid={self._secret}&{self._metrics}')
  
  def get_city_temperature(self, city=None, lat=None, lon=None):
    city_info = self._get_city_info(city, lat, lon).json()
    return city_info['main']['temp']