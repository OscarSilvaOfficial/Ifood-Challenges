from app.infra import mount_app 
from app.infra.configs.enviroment import DEBUG
import uvicorn

app = mount_app()

if __name__ == '__main__':
  uvicorn.run(app, host="0.0.0.0", port=8000)