from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .post_model import PostModel


class UserBase(SQLModel):
    full_name: str
    username: str
    email: str
    disabled: bool = False


class UserModel(UserBase, table=True):
    __tablename__ = "user"
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    posts: List["PostModel"] = Relationship(back_populates="creator_user")


class UserCreate(UserBase):
    hashed_password: str


class UserRead(UserBase):
    id: int


class UserUpdate(UserBase):
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    disabled: Optional[bool] = None


class UserPassUpdate(SQLModel):
    hashed_password: str
