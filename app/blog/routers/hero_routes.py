from typing import List
from fastapi import APIRouter, status
from app.blog.models.hero_model import HeroCreate, HeroRead
from app.blog.controllers import (
    add_hero_controller,
    show_hero_controller,
    get_all_heros_controller
)


router = APIRouter(
    prefix="/blog/hero",
    tags=['Hero'],
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def add(request: HeroCreate):
    return add_hero_controller.invoke(request)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[HeroRead])
def all():
    return get_all_heros_controller.invoke()


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=HeroRead)
def show(id: int):
    return show_hero_controller.invoke(id)
