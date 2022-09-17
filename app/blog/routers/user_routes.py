from typing import List
from fastapi import APIRouter, status, Query
from app.blog.models.user_model import UserRead, UserCreate, UserUpdate
from app.blog.controllers import user_controller


router = APIRouter(
    prefix="/users",
    tags=['User']
)


@router.post("/",
             response_model=UserRead,
             status_code=status.HTTP_201_CREATED
             )
def add(*, user: UserCreate):
    return user_controller.add_user(user)


@router.get("/",
            response_model=List[UserRead],
            status_code=status.HTTP_200_OK
            )
def all(
    *,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    return user_controller.get_all_users(offset, limit)


@router.get("/{id}",
            response_model=UserRead,
            status_code=status.HTTP_200_OK
            )
def show(*, id: int):
    return user_controller.get_user(id)


@router.patch("/{team_id}",
              response_model=UserRead,
              status_code=status.HTTP_200_OK
              )
def update(
    *,
    id: int,
    user: UserUpdate,
):
    return user_controller.update_user(id, user)


@router.delete("/{id}",
               status_code=status.HTTP_200_OK
               )
def delete(*, id: int):
    return user_controller.detete_user(id)

