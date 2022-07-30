from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.core.user import User
from app.core.hashing import verify_password
from app.core.token import TokenData
from app.config import cfg
import app.core.constants as const
from app.core.user import get_user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# get_user = cfg.APP_SETTING.GET_USER_METHOD


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=const.HTTP_401_UNAUTHORIZED_DETAIL_GET_CURRENT_USER,
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, cfg.APP_SETTING.SECRET_KEY, algorithms=[
                             cfg.APP_SETTING.JWT_ENCODE_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=400, detail=const.HTTP_EXCEPTION_400_INACTIVE_USER)
    return current_user
