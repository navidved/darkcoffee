from typing import List
from fastapi import APIRouter, status, Query, Depends

from services.game.models.hero_model import HeroRead, HeroCreate, HeroReadWithTeam, HeroUpdate, HeroModel
import services.game.controllers.hero_controller as hero_controller
from core.authentication import authenticate_user, get_current_active_user

from core.database import Database


router = APIRouter(
    prefix="/blog/heros",
    tags=['Hero'],
)


@router.post("/",
             response_model=HeroReadWithTeam,
             status_code=status.HTTP_201_CREATED
             )
async def add_hero(*, hero: HeroCreate, current_user = Depends(get_current_active_user)):
    return hero_controller.add_hero(hero)


@router.get("/",
            response_model=List[HeroReadWithTeam],
            status_code=status.HTTP_200_OK,
            )
async def get_all_heros(
    *,
    offset: int = 0,
    limit: int = Query(default=10, lte=15)
    
):
    return hero_controller.get_all_heros(offset, limit)


@router.get("/{id}",
            response_model=HeroReadWithTeam,
            status_code=status.HTTP_200_OK
            )
async def get_hero(*, id: int):
    session = Database().get_session()
    hero = session.get(HeroModel, id)
    return hero


@router.patch("/{hero_id}",
              response_model=HeroRead,
              status_code=status.HTTP_200_OK
              )
async def update_hero(
    *,
    id: int,
    hero: HeroUpdate,
):
    return hero_controller.update_hero(id, hero)


@router.delete("/{id}",
               status_code=status.HTTP_200_OK
               )
async def detete_hero(*, id: int):
    return hero_controller.detete_hero(id)