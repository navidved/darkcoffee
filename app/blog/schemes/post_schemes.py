from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    body: str


class Post(PostBase):
    class Config():
        orm_mode = True


class ShowPost(BaseModel):
    from app.blog.schemes.user_schemes import ShowUser
    id: int
    title: str
    body: str
    creator_user: ShowUser

    class Config():
        orm_mode = True
