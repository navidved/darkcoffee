from app.blog.repository.hero_repo import HeroRepo
from app.blog.models.hero_model import HeroRead
from typing import List
from fastapi import HTTPException, status


def invoke() -> List[HeroRead]:
    heros = HeroRepo().get_all_heros()
    if not heros:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No heros found.")
    return heros