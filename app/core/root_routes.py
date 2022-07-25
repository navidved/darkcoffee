from fastapi import APIRouter
from app.config import settings
import app.core.database as db


router = APIRouter(
    prefix="",
    tags=['Root']
)


@router.get('/')
def root():
    return {"app": settings.AppConfig().APP_NAME}


@router.get('/migrate')
def migrate():
    db.migrate()
    return {"migrate": "done!"}
