from typing import List
from fastapi import APIRouter, status, Query
from app.blog.models.hero_model import HeroCreate, HeroRead, HeroReadWithTeam, HeroUpdate, HeroModel
from app.blog.models.team_model import TeamModel
from app.blog.controllers import hero_controller



router = APIRouter(
    prefix="/blog/heros",
    tags=['Hero'],
)


@router.post("/",
             response_model=HeroRead,
             status_code=status.HTTP_201_CREATED
             )
def add(*, hero: HeroCreate):
    return hero_controller.add_hero(hero)


@router.post("/with-team",
             status_code=status.HTTP_201_CREATED
             )
def new_hero():
    from app.core.database import Database, Session
    session = Session(Database().engine)
    with session:
        barca_team = TeamModel(name="FC Barcelona", headquarters="Catalonia")
        barca_hero = HeroModel(
            name="Messi", secret_name="MazMaz", team=barca_team
        )

        session.add(barca_hero)
        session.commit()
        session.refresh(barca_hero)
    return barca_hero


@router.get("/",
            response_model=List[HeroRead],
            status_code=status.HTTP_200_OK
            )
def all(
    *,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    return hero_controller.get_all_heros(offset, limit)


@router.get("/{id}",
            response_model=HeroReadWithTeam,
            status_code=status.HTTP_200_OK
            )
def show(*, id: int):
    return hero_controller.get_hero(id)


@router.patch("/{hero_id}",
              response_model=HeroRead,
              status_code=status.HTTP_200_OK
              )
def update(
    *,
    id: int,
    hero: HeroUpdate,
):
    return hero_controller.update_hero(id, hero)


@router.delete("/{id}",
               status_code=status.HTTP_200_OK
               )
def delete(*, id: int):
    return hero_controller.detete_hero(id)
