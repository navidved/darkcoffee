from typing import List
from pydantic import BaseModel


class UserSchema(BaseModel):
    full_name: str
    username: str
    email: str
    password: str


class ShowUserSchema(BaseModel):
    # from app.blog.schemes.post_schemes import PostSchema
    full_name: str
    username: str
    email: str
    disabled: bool
    # posts: List[PostSchema] = []

    class Config():
        orm_mode = True
