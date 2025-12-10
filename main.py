from uvicorn import run

from src.infrastructure.config import env
from src.presentation.app import app

if __name__ == "__main__":
    run(
        app, 
        host=env.app.host, 
        port=env.app.port
    )