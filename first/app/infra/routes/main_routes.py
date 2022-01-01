from typing import Optional
from fastapi import HTTPException
from app.useCases.services.tracks_service import TracksService
import logging

logger = logging.getLogger(__name__)

def main_routes(router):
  
  @router.get('/')
  async def get_playlist(city: Optional[str]=None, lat: Optional[str]=None, lon: Optional[str]=None):
    
    if not city and (not lat or not lon):
      raise HTTPException(status_code=404, detail="Inform city or lat and lon")
    
    logger.info("\ncity: %s, lat: %s, lon: %s", city, lat, lon)
    
    tracks_service = TracksService()
    return tracks_service.get(city, lat, lon)
  return router