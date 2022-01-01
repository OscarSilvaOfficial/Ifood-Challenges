from abc import ABC, abstractmethod

class WSGIApplication(ABC):
  
  """
  Método deve montar a instancia do servidor HTTP
  """
  @abstractmethod
  def mount(self):
    pass
  
  """
  Método deve deve retornar uma instância da classe contruída
  """
  @abstractmethod
  def factory():
    pass