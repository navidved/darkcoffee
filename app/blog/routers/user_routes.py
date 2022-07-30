from typing import List
from fastapi import APIRouter, status
from app.blog.schemes.user_schemes import ShowUserSchema, UserSchema
from app.blog.repository.user_repo import UserRepo


router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.get('/', response_model=List[ShowUserSchema])
def all():
    return UserRepo().get_all_users()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowUserSchema)
def add(request: UserSchema):
    return UserRepo().add_user(request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUserSchema)
def show(id: int):
    return UserRepo().show_user(id)


@router.get('/find/{username}', status_code=status.HTTP_200_OK, response_model=ShowUserSchema)
def find(username: str):
    return UserRepo().get_user(username)
