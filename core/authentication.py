from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from core.hashing import verify_password
from core.token import TokenData
from config import config
from core.base_constant import const
import importlib


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
auth_user_module = importlib.import_module(config.AUTH_USER_MODULE)
auth_user_method = getattr(auth_user_module, config.AUTH_USER_METHOD)


def authenticate_user(username: str, password: str):
    user = auth_user_method(username)
    hashed_password_attr = getattr(user, config.AUTH_USER_HASSHED_PASS_FIELD)
    if not user:
        return False
    if not verify_password(password, hashed_password_attr):
        return False
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=const.HTTP_401_UNAUTHORIZED_DETAIL_GET_CURRENT_USER,
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[
                             config.JWT_ENCODE_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = auth_user_method(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user = Depends(get_current_user)):
    current_user_disabled_attr = getattr(current_user, config.AUTH_USER_DISABLED_FIELD)
    if current_user_disabled_attr:
        raise HTTPException(
            status_code=400, detail=const.HTTP_EXCEPTION_400_INACTIVE_USER)
    return current_user
