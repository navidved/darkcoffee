from typing import TYPE_CHECKING ,List , Optional
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .post_model import Post


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    username: str
    email: str
    disabled: bool = False
    hashed_password: str
    posts: List["Post"] = Relationship(back_populates="creator_user")

