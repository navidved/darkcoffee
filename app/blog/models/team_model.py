from typing import List, Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .hero_model import HeroModel


class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class TeamModel(TeamBase, table=True):
    __tablename__ = "team"
    id: Optional[int] = Field(default=None, primary_key=True)
    heroes: List["HeroModel"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: int


class TeamUpdate(SQLModel):
    name: Optional[str] = None
    headquarters: Optional[str] = None


class TeamReadWithHeroes(TeamRead):
    from app.blog.models.hero_model import HeroRead
    heroes: List[HeroRead] = []