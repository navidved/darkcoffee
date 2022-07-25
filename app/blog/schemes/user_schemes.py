from typing import List
from pydantic import BaseModel


class User(BaseModel):
    full_name: str
    username: str
    email: str
    password: str


class ShowUser(BaseModel):
    from app.blog.schemes.post_schemes import Post
    full_name: str
    username: str
    email: str
    disabled: bool
    posts: List[Post] = []

    class Config():
        orm_mode = True
