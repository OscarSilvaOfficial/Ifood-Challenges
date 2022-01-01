from abc import ABC, abstractmethod

class UseCases(ABC):
  
  @abstractmethod
  def get(self, id):
    pass
