from typing import Optional
from app.adapters.repositories.interfaces.repository import Repository
import sqlite3

class SQLiteRepository(Repository):
  
  def __init__(self, entity, db_path='local.db'):
    self._connection = db_path  
    self._entity = entity
    
  def connect(self):
    connection = sqlite3.connect(self._connection)
    return connection.cursor()
  
  def get(self, id: Optional[int] = None):
    pass
    
  def create(self, data):
    pass

  def update(self, id, data):
    pass

  def delete(self, id):
    pass