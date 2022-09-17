from typing import List
from app.blog.repository.post_repo import PostRepo
from app.blog.models.post_model import PostUpdate, PostCreate, PostRead
from fastapi import HTTPException, status
from app.core.user import User


def update_post(id: int, post: PostUpdate) -> PostRead:
    updated_post = PostRepo().update_post(id, post)
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return updated_post


def add_post(post: PostCreate, current_user: User) -> PostRead:
    return PostRepo().add_post(post, current_user)


def get_post(id: int) -> PostRead:
    post = PostRepo().get_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


def get_all_posts(offset: int, limit: int) -> List[PostRead]:
    posts = PostRepo().get_all_posts(offset, limit)
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Post found.")
    return posts


def detete_post(id: int):
    detete_result = PostRepo().delete_post(id)
    if not detete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return detete_result
