import sqlite3
from app.infra.db.interfaces.db import DB

class SQLite(DB):
  
  def __init__(self, connection='local.db'):
    self._connection = connection  
    
  def connect(self):
    connection = sqlite3.connect(self._connection)
    return connection.cursor()
