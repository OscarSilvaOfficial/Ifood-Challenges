from typing import Optional
from app.adapters.repositories.interfaces.repository import Repository
from app.useCases.services.interfaces.userCases import UseCases

class TracksService(UseCases):
  
  def __init__(self, repository: Repository):
    self.repository = repository
    
  def get(self, id: Optional[int] = None):
    return self.repository.get(id)
    
  def create(self, data):
    return self.repository.create(data)
    
  def update(self, id, data):
    return self.repository.update(id, data)
    
  def delete(self, id):
    return self.repository.delete(id)