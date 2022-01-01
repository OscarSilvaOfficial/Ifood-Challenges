from app.infra.main import MainServer
from app.infra.http.fastapi import FastAPIServer
from app.infra.routes.main_routes import main_routes
from fastapi import APIRouter

def mount_routes(app, router=None):
  router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
  )
  routes = main_routes(router)
  app.include_router(routes)

def mount_app():
  server = MainServer(FastAPIServer)
  app = server.app
  mount_routes(app)
  return app