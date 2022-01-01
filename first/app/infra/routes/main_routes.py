from app.useCases.services.tracks_service import TracksService


def main_routes(app):
  
  @app.get('/')
  async def all_traks():
    tracks_service = TracksService()
    return tracks_service.get()