from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .user_model import UserModel


class PostBase(SQLModel):
    title: str
    body: str


class PostModel(PostBase, table=True):
    __tablename__ = "post"
    id: Optional[int] = Field(default=None, primary_key=True)
    author: Optional["UserModel"] = Relationship(back_populates="posts")
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    author: Optional["UserModel"] = Relationship(back_populates="posts")


class PostUpdate(PostBase):
    title: Optional[str] = None
    body: Optional[str] = None
