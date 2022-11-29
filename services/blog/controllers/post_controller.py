from fastapi import HTTPException, status
from typing import List
from services.blog.repository.post_repo import PostRepo
from services.blog.models.post_model import PostUpdate, PostCreate, PostRead
from services.blog.models.agent_model import AgentRead
from .blog_constant import blog_const


def update_post(id: int, post: PostUpdate) -> PostRead:
    updated_post = PostRepo().update_post(id, post)
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=blog_const.POST_NOT_FOUND)
    return updated_post


def add_post(post: PostCreate, current_user: AgentRead) -> PostRead:
    return PostRepo().add_post(post, current_user)


def get_post(id: int) -> PostRead:
    post = PostRepo().get_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=blog_const.POST_NOT_FOUND)
    return post


def get_all_posts(offset: int, limit: int) -> List[PostRead]:
    posts = PostRepo().get_all_posts(offset, limit)
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=blog_const.NO_POST_EXIST)
    return posts


def detete_post(id: int):
    detete_result = PostRepo().delete_post(id)
    if not detete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=blog_const.POST_NOT_FOUND)
    return detete_result
