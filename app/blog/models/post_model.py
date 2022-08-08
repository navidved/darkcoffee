from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .user_model import UserModel


class PostBase(SQLModel):
    title: str
    body: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class PostModel(PostBase, table=True):
    __tablename__ = "post"
    id: Optional[int] = Field(default=None, primary_key=True)
    creator_user: Optional["UserModel"] = Relationship(back_populates="posts")


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int


class PostUpdate(PostBase):
    title: Optional[str] = None
    body: Optional[str] = None
    user_id: Optional[int] = None