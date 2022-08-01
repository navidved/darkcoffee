from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .user_model import UserModel


class PostModel(SQLModel, table=True):
    __tablename__ = "Post"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    body: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    creator_user: Optional["UserModel"] = Relationship(back_populates="posts")
