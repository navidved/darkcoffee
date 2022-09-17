from typing import List
from app.blog.repository.user_repo import UserRepo
from app.blog.models.user_model import UserUpdate, UserCreate, UserRead
from fastapi import HTTPException, status


def update_user(id: int, user: UserUpdate) -> UserRead:
    updated_user = UserRepo().update_user(id, user)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated_user


def add_user(user: UserCreate) -> UserRead:
    return UserRepo().add_user(user)


def get_user(id: int) -> UserRead:
    user = UserRepo().get_user(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


def get_all_users(offset: int, limit: int) -> List[UserRead]:
    users = UserRepo().get_all_users(offset, limit)
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No User found.")
    return users


def detete_user(id: int):
    detete_result = UserRepo().delete_user(id)
    if not detete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return detete_result
