from fastapi import APIRouter
from app.config import settings
import app.core.database as db


router = APIRouter(
    prefix="",
    tags=['Root']
)


@router.get('/')
def root():
    return {"app": settings.app_name}


@router.get('/migrate')
def migrate():
    db.migrate()
    return {"migrate":"done!"}