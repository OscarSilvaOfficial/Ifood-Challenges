from typing import Optional
from .interfaces.location import LocationModel as ILocation

class Location(ILocation):
  city: Optional[str]
  lat:  Optional[str]
  lon:  Optional[str]