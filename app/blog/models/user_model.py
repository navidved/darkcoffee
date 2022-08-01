from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .post_model import PostModel


class UserModel(SQLModel, table=True):
    __tablename__ = "User"
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    username: str
    email: str
    disabled: bool = False
    hashed_password: str
    posts: List["PostModel"] = Relationship(back_populates="creator_user")
