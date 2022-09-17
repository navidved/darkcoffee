from typing import List
from fastapi import APIRouter, status, Query, Depends
from app.blog.controllers import post_controller
from app.blog.models.post_model import PostCreate, PostRead, PostUpdate
from app.core.user import User
from app.core.authentication import authenticate_user, get_current_active_user


router = APIRouter(
    prefix="/blog/posts",
    tags=['Post'],
)


@router.post("/",
             response_model=PostRead,
             status_code=status.HTTP_201_CREATED
             )
def add(
    *,
    post: PostCreate,
    current_user: User = Depends(get_current_active_user)
):
    return post_controller.add_post(post, current_user)


@router.get("/",
            response_model=List[PostRead],
            status_code=status.HTTP_200_OK
            )
def all(
    *,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    return post_controller.get_all_posts(offset, limit)


@router.get("/{id}",
            response_model=PostRead,
            status_code=status.HTTP_200_OK
            )
def show(*, id: int):
    return post_controller.get_post(id)


@router.patch("/{post_id}",
              response_model=PostRead,
              status_code=status.HTTP_200_OK
              )
def update(
    *,
    id: int,
    post: PostUpdate,
):
    return post_controller.update_post(id, post)


@router.delete("/{id}",
               status_code=status.HTTP_200_OK
               )
def delete(*, id: int):
    return post_controller.detete_post(id)
