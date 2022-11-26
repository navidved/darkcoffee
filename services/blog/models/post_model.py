from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from .agent_model import AgentModel


class PostBase(SQLModel):
    title: str
    body: str


class PostModel(PostBase, table=True):
    __tablename__ = "post"
    id: Optional[int] = Field(default=None, primary_key=True)
    author_id: Optional[int] = Field(default=None, foreign_key="agent.id")
    author: Optional["AgentModel"] = Relationship(back_populates="posts")


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    author: Optional["AgentModel"] = Relationship(back_populates="posts")


class PostReadWithAgent(PostRead):
    from services.blog.models.agent_model import AgentRead
    author: Optional[AgentRead] = None


class PostUpdate(PostBase):
    title: Optional[str] = None
    body: Optional[str] = None
