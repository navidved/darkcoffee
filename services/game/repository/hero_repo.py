from sqlmodel import select
from core.database import Database

from services.game.models.hero_model import HeroModel, HeroCreate, HeroRead, HeroUpdate


class HeroRepo:

    def new_hero(self,
                 hero: HeroCreate
                 ) -> HeroModel:
        session = Database().get_session()
        db_hero = HeroModel.from_orm(hero)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero

    def get_all_heros(self,
                      offset: int,
                      limit: int
                      ) -> list[HeroRead]:
        session = Database().get_session()
        statement = select(HeroModel).offset(offset).limit(limit)
        heros = session.exec(statement).all()
        return heros

    def get_hero(self,
                 id: int
                 ) -> HeroRead:
        session = Database().get_session()
        data = session.get(HeroModel, id)
        return data

    def update_hero(self,
                    id: int,
                    hero: HeroUpdate
                    ) -> HeroRead:
        session = Database().get_session()
        db_hero = session.get(HeroModel, id)
        if not db_hero:
            return None

        hero_data = hero.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_hero, key, value)

        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero

    def delete_hero(self,
                    id: int
                    ) -> bool:
        session = Database().get_session()
        hero = session.get(HeroModel, id)
        if not hero:
            return False
        session.delete(hero)
        session.commit()
        return True
