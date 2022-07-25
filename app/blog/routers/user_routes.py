from typing import List
from fastapi import APIRouter, status
from app.blog.schemas import user_schemas
from app.blog.repository.user_repo import UserRepo


router = APIRouter(
    prefix="/user",
    tags=['User']
)

@router.get('/', response_model=List[user_schemas.ShowUser])
def all():
    return UserRepo().get_all_users()


@router.post('/', status_code=status.HTTP_201_CREATED)
def add(request: user_schemas.User):
    return UserRepo().add_user(request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=user_schemas.ShowUser)
def show(id: int):
    return UserRepo().show_user(id)