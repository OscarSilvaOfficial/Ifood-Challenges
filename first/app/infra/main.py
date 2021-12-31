from app.infra.interfaces.WSGIApplication import WSGIApplication

class MainServer:
  
  def __init__(self, http_server: WSGIApplication) -> None:
      self._http_server = http_server
  
  @property
  def app(self):
    return self._http_server.factory()