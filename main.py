from src.router import api_v1
from src.config import settings
from fastapi import FastAPI
import uvicorn


app = FastAPI(
    debug=settings.DEBUG
)
app.include_router(api_v1)


if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )
