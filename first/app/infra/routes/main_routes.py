from starlette.routing import request_response
from app.useCases.services.tracks_service import TracksService


def main_routes(router):
  
  @router.get('/')
  async def all_traks():
    tracks_service = TracksService()
    return tracks_service.get()
  
  return router