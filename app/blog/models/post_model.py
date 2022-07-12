from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .user_model import User


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    body: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    creator_user: Optional["User"] = Relationship(back_populates="posts")
