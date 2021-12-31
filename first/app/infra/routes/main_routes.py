from app.adapters.repositories.sqlite import SQLiteRepository
from app.entities.interfaces.tracks import TracksModel
from app.useCases.services.tracks_service import TracksService


def main_routes(app):
  
  @app.get('/')
  async def all_traks():
    tracks_service = TracksService(SQLiteRepository(entity=TracksModel))
    return tracks_service.get()