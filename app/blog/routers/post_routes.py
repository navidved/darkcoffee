from typing import List
from fastapi import APIRouter, status, Depends
from app.blog.schemes.post_schemes import PostBaseSchema
from app.blog.controllers import (
    add_post_controller,
    get_all_posts_controller,
    show_post_controller,
    update_post_controller,
    delete_post_controller
)
from app.blog.models import post_model
from app.core.user import User
from app.core.authentication import authenticate_user, get_current_active_user


router = APIRouter(
    prefix="/blog/post",
    tags=['Post'],
)


@router.get('/', response_model=List[post_model.Post])
def all(current_user: User = Depends(get_current_active_user)):
    return get_all_posts_controller.invoke()


@router.post('/', status_code=status.HTTP_201_CREATED)
def add(request: post_model.Post):
    return add_post_controller.invoke(request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=post_model.Post)
def show(id: int):
    return show_post_controller.invoke(id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, post_data: PostBaseSchema):
    return update_post_controller.invoke(id, post_data)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def destroy(id: int):
    return delete_post_controller.invoke(id)
