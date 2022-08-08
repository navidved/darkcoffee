from app.blog.repository.hero_repo import HeroRepo
from app.blog.models.hero_model import HeroRead
from fastapi import HTTPException, status


def invoke(id: int) -> HeroRead:
    hero = HeroRepo().get_hero(id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hero not found")
    return hero