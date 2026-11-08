from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import Base, engine
from .error_handlers import register_exception_handlers
from .routers import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)  # tu tao bang neu chua co
    yield


app = FastAPI(title="Gia sư AI API", version="1.0.0", lifespan=lifespan)
app.include_router(auth.router)
register_exception_handlers(app)
