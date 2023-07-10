from fastapi import FastAPI

from app.core.db import Base, get_async_session
from app.core.user import current_superuser, current_user
from app.main import app

app = FastAPI()
