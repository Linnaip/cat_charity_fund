from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from app.core.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

