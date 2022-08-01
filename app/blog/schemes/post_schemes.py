from pydantic import BaseModel
from typing import Optional



class PostBaseSchema(BaseModel):
    title: str
    body: str


class PostSchema(PostBaseSchema):
    class Config():
        orm_mode = True


class ShowPostSchema(BaseModel):
    id: int
    title: str
    body: str
    creator_user: Optional["ShowUserSchema"]

    class Config():
        orm_mode = True


from app.blog.schemes.user_schemes import ShowUserSchema
ShowPostSchema.update_forward_refs()