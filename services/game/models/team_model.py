from typing import List, Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .hero_model import HeroModel
    from services.blog.models.agent_model import AgentModel


class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class TeamModel(TeamBase, table=True):
    __tablename__ = "team"
    id: Optional[int] = Field(default=None, primary_key=True)
    heroes: List["HeroModel"] = Relationship(back_populates="team", sa_relationship_kwargs={"lazy": "joined"})
    agent_id: Optional[int] = Field(default=None, foreign_key="agent.id")
    agent: Optional["AgentModel"] = Relationship(sa_relationship_kwargs={"lazy": "joined"})


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: int

class TeamReadWithAgent(TeamRead):
    from services.blog.models.agent_model import AgentRead
    agent: Optional[AgentRead] = None


class TeamUpdate(SQLModel):
    name: Optional[str] = None
    headquarters: Optional[str] = None


class TeamReadWithHeroes(TeamRead):
    from services.game.models.hero_model import HeroRead
    heroes: List[HeroRead] = []


