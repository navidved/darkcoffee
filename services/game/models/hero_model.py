from typing import Optional, TYPE_CHECKING, List
from sqlmodel import Field, SQLModel, Relationship
if TYPE_CHECKING:
    from .team_model import TeamModel


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int]
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


class HeroModel(HeroBase, table=True):
    __tablename__ = "hero"
    id: Optional[int] = Field(default=None, primary_key=True)
    team: Optional["TeamModel"] = Relationship(back_populates="heroes", sa_relationship_kwargs={"lazy": "joined"})


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[int] = None


class HeroReadWithTeam(HeroRead):
    from services.game.models.team_model import TeamRead
    team: Optional[TeamRead] = None


class HeroReadWithTeam(HeroRead):
    from services.game.models.team_model import TeamReadWithAgent
    team: Optional[TeamReadWithAgent] = None

    