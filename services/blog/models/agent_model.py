from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .post_model import PostModel


class AgentBase(SQLModel):
    full_name: Optional[str]
    company: Optional[str]
    username: str = Field(index=True)
    email: str = Field(index=True)
    disabled: bool = False


class AgentModel(AgentBase, table=True):
    __tablename__ = "agent"
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: Optional[str]
    posts: List["PostModel"] = Relationship(back_populates="author")


class AgentCreate(AgentBase):
    password: str


class AgentRead(AgentBase):
    id: int

class AgentUpdate(AgentBase):
    full_name: Optional[str] = None
    email: Optional[str] = None
    disabled: Optional[bool] = None
    company: Optional[bool] = None


class AgentPassUpdate(SQLModel):
    hashed_password: str


class AgentReadWithPosts(AgentRead):
    from services.blog.models.post_model import PostRead
    posts: List[PostRead] = []
