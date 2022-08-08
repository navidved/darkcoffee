from app.blog.models.hero_model import HeroModel, HeroCreate, HeroRead
from app.core.repo import Repo
from sqlmodel import select


class HeroRepo(Repo):
    def add_hero(self, hero: HeroCreate) -> HeroModel:
        db_hero = HeroModel.from_orm(hero)
        self.session.add(db_hero)
        self.session.commit()
        self.session.refresh(db_hero)
        return db_hero


    def get_all_heros(self) -> list[HeroRead]:
        statement = select(HeroModel)
        heros = self.session.exec(statement).all()
        return heros


    def get_hero(self, id: int) -> HeroRead:
        return self.session.get(HeroModel, id)