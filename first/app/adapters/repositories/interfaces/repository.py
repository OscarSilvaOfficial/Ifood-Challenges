from abc import ABC, abstractmethod

class Repository(ABC):
  
  @abstractmethod
  def get(self, id):
    pass
  
  @abstractmethod
  def create(self, data):
    pass

  @abstractmethod
  def update(self, id, data):
    pass

  @abstractmethod
  def delete(self, id):
    pass