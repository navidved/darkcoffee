from typing import List
from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    password:str
    

class ShowUser(BaseModel):
    from app.blog.schemas.post_schemas import Post
    name:str
    email:str
    posts : List[Post] =[]
    class Config():
        orm_mode = True
