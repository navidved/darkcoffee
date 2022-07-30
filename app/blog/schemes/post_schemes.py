from pydantic import BaseModel


class PostBaseSchema(BaseModel):
    title: str
    body: str


class PostSchema(PostBaseSchema):
    class Config():
        orm_mode = True


class ShowPostSchema(BaseModel):
    # from app.blog.schemes.user_schemes import ShowUserSchema
    id: int
    title: str
    body: str
    # creator_user: ShowUserSchema

    class Config():
        orm_mode = True
