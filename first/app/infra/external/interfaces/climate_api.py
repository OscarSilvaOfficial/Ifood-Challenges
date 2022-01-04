from abc import ABC, abstractmethod

class ClimateAPI(ABC):
  
  @abstractmethod
  def get_city_temperature(self, city, lat, lon):
    pass