from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session

router = APIRouter()


@router.get('/')
async def get_charity_projects():
    pass


@router.post('/')
async def create_charity_project():
    pass


@router.patch('/')
async def update_charity_project():
    pass


@router.delete('/')
async def delete_charity_project():
    pass
