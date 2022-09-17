from typing import List
from fastapi import APIRouter, status, Query
from app.blog.models.team_model import TeamCreate, TeamRead, TeamReadWithHeroes, TeamUpdate
from app.blog.controllers import team_controller


router = APIRouter(
    prefix="/blog/teams",
    tags=['Team'],
)


@router.post("/",
             response_model=TeamReadWithHeroes,
             status_code=status.HTTP_201_CREATED
             )
def add(*, team: TeamCreate):
    return team_controller.add_team(team)


@router.get("/",
            response_model=List[TeamReadWithHeroes],
            status_code=status.HTTP_200_OK
            )
def all(
    *,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    return team_controller.get_all_teams(offset, limit)


@router.get("/{id}",
            response_model=TeamReadWithHeroes,
            status_code=status.HTTP_200_OK
            )
def show(*, id: int):
    return team_controller.get_team(id)


@router.patch("/{team_id}",
              response_model=TeamReadWithHeroes,
              status_code=status.HTTP_200_OK
              )
def update(
    *,
    id: int,
    team: TeamUpdate,
):
    return team_controller.update_team(id, team)


@router.delete("/{id}",
               status_code=status.HTTP_200_OK
               )
def delete(*, id: int):
    return team_controller.detete_team(id)
