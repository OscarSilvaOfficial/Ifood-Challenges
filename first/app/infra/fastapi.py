from app.infra.interfaces.WSGIApplication import WSGIApplication
from fastapi import FastAPI

class FastAPIServer(WSGIApplication):
  
  def __init__(self, api):
    self._api=api
  
  def mount(self):
    return self._api
  
  @staticmethod
  def factory():
    api = FastAPIServer(api=FastAPI())
    return api.mount()
