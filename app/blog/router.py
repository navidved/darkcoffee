from msilib import schema
from typing import List
from fastapi import APIRouter, Depends, status
from app.blog import schemas
from app.blog.controllers import add_post_controller, get_all_posts_controller, show_post_controller, update_post_controller, delete_post_controller
from sqlalchemy.orm import Session
from app.blog.models import post_model


router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)


@router.get('/', response_model=List[schemas.ShowPost])
def all():
    return get_all_posts_controller.__invoke()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: post_model.Post):
    return add_post_controller.__invoke(request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowPost)
def show(id: int):
    return show_post_controller.__invoke(id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, post_data: schemas.PostBase):
    return update_post_controller.__invoke(id, post_data)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def destroy(id: int):
    return delete_post_controller.__invoke(id)