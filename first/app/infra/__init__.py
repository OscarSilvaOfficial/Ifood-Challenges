from app.infra.main import MainServer
from app.infra.http.fastapi import FastAPIServer
from app.infra.routes.main_routes import main_routes

def mount_app():
  server = MainServer(FastAPIServer)
  app = server.app
  main_routes(app)
  return app