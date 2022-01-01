from typing import Optional
from pydantic import BaseModel

class LocationModel(BaseModel):
  city: Optional[str]
  lat:  Optional[str]
  lon:  Optional[str]