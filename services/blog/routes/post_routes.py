from typing import List
from fastapi import APIRouter, status, Query, Depends
import services.blog.controllers.post_controller as post_controller
from services.blog.models.post_model import PostCreate, PostRead, PostUpdate, PostReadWithAgent
from services.blog.models.agent_model import AgentRead
from core.authentication import authenticate_user, get_current_active_user


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
    current_user: AgentRead = Depends(get_current_active_user)
):
    return post_controller.add_post(post, current_user)


@router.get("/",
            response_model=List[PostReadWithAgent],
            status_code=status.HTTP_200_OK
            )
def get_all_posts(
    *,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    return post_controller.get_all_posts(offset, limit)


@router.get("/{id}",
            response_model=PostReadWithAgent,
            status_code=status.HTTP_200_OK
            )
def get_post(*, id: int):
    return post_controller.get_post(id)


@router.patch("/{post_id}",
              response_model=PostRead,
              status_code=status.HTTP_200_OK
              )
def update_post(
    *,
    id: int,
    post: PostUpdate,
):
    return post_controller.update_post(id, post)


@router.delete("/{id}",
               status_code=status.HTTP_200_OK
               )
def detete_post(*, id: int):
    return post_controller.detete_post(id)
