from typing import Optional
from app.adapters.repositories.interfaces.repository import Repository as IRepository
from app.infra.db.interfaces.db import DB

class Repository(IRepository):
  
  def __init__(self, db: DB, entity):
    self._db=db
    self._entity=entity
  
  def get(self, id: Optional[int] = None):
    pass
    
  def create(self, data):
    pass

  def update(self, id, data):
    pass

  def delete(self, id):
    pass