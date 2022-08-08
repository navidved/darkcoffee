from app.blog.repository.hero_repo import HeroRepo
from app.blog.models.hero_model import HeroCreate, HeroModel


def invoke(request: HeroCreate) -> HeroModel:
    return HeroRepo().add_hero(request)