from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .post_model import PostModel


class UserBase(SQLModel):
    username: str = Field(index=True)
    email: str = Field(index=True)
    full_name: str
    disabled: bool = False


class UserModel(UserBase, table=True):
    __tablename__ = "user"
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: Optional[str]
    posts: List["PostModel"] = Relationship(back_populates="author")


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


class UserUpdate(UserBase):
    full_name: Optional[str] = None
    email: Optional[str] = None
    disabled: Optional[bool] = None


class UserPassUpdate(SQLModel):
    hashed_password: str
