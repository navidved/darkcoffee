from datetime import datetime, timedelta
from jose import jwt
from pydantic import BaseModel
from app.config import cfg


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, cfg.APP_SETTING.SECRET_KEY,
                             algorithm= cfg.APP_SETTING.JWT_ENCODE_ALGORITHM)
    return encoded_jwt
