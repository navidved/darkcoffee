from os import path
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import FileResponse

from core.token import Token, create_access_token
from core.authentication import authenticate_user
from config import config
from core.base_constant import const


router = APIRouter(
    prefix="",
    tags=['Root']
)


@router.get('/')
def root():
    return {"app": config.APP_NAME}


@router.get('/migrate')
def migrate():
    from core.database import Database
    Database().migrate()
    return {"database": "migrated"}


@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(config.FAVICON_PATH)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=const.HTTP_401_UNAUTHORIZED_DETAIL_AUTH_USER,
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
