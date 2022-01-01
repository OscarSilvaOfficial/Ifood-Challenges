from app.infra.http.interfaces.WSGIApplication import WSGIApplication
from fastapi import APIRouter, FastAPI

class FastAPIServer(WSGIApplication):
  
  def __init__(self, api):
    self._api=api
  
  def mount(self):
    return self._api
  
  @staticmethod
  def factory():
    api = FastAPIServer(api=FastAPI())
    return api.mount()
