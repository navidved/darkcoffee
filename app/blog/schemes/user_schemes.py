# from typing import List, Optional
# from pydantic import BaseModel

    

# class UserSchema(BaseModel):
#     full_name: str
#     username: str
#     email: str
#     password: str


# class ShowUserSchema(BaseModel):
#     id: int
#     full_name: str
#     username: str
#     email: str
#     disabled: bool
#     posts: Optional[List["PostSchema"]] = []

#     class Config():
#         orm_mode = True


# from app.blog.schemes.post_schemes import PostSchema
# ShowUserSchema.update_forward_refs()