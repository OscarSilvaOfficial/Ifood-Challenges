from logging import raiseExceptions
from app.infra.fastapi import FastAPIServer

app = FastAPIServer.factory()

@app.get('/')
async def index():
  return 'ok'