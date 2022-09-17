from app.blog.models.hero_model import HeroModel, HeroCreate, HeroRead, HeroUpdate
from app.core.repo import Repo
from sqlmodel import select


class HeroRepo(Repo):
    def add_hero(self, hero: HeroCreate) -> HeroModel:
        db_hero = HeroModel.from_orm(hero)
        self.session.add(db_hero)
        self.session.commit()
        self.session.refresh(db_hero)
        return db_hero


    def get_all_heros(self, offset: int, limit: int) -> list[HeroRead]:
        statement = select(HeroModel).offset(offset).limit(limit)
        heros = self.session.exec(statement).all()
        return heros


    def get_hero(self, id: int) -> HeroRead:
        return self.session.get(HeroModel, id)

    
    def update_hero(self, id: int, hero: HeroUpdate) -> HeroRead:
        db_hero = self.session.get(HeroModel, id)
        if not db_hero:
            return None
        
        hero_data = hero.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_hero, key, value)
        
        self.session.add(db_hero)
        self.session.commit()
        self.session.refresh(db_hero)
        return db_hero


    def delete_hero(self, id: int) -> bool:
        hero = self.session.get(HeroModel, id)
        if not hero:
            return False
        self.session.delete(hero)
        self.session.commit()
        return True