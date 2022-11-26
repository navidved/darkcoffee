from typing import List
from fastapi import HTTPException, status

from services.game.repository.hero_repo import HeroRepo
from services.game.models.hero_model import HeroUpdate, HeroCreate, HeroRead


def update_hero(id: int, hero: HeroUpdate) -> HeroRead:
    updated_hero = HeroRepo().update_hero(id, hero)
    if not updated_hero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hero not found")
    return updated_hero


def add_hero(hero: HeroCreate) -> HeroRead:
    return HeroRepo().new_hero(hero)


def get_hero(id: int) -> HeroRead:
    hero = HeroRepo().get_hero(id)
    if not hero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hero not found")
    return hero


def get_all_heros(offset: int, limit: int) -> List[HeroRead]:
    heros = HeroRepo().get_all_heros(offset, limit)
    if not heros:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Hero found.")
    return heros


def detete_hero(id: int):
    detete_result = HeroRepo().delete_hero(id)
    if not detete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hero not found")
    return detete_result
