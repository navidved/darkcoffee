from typing import Optional
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str = Field(index=True)
    disabled: bool = False
    full_name: str | None = None


class UserInDB(UserBase):
    hashed_password: Optional[str]


def get_user(username: str) -> UserInDB:
    from config import config
    db = config.STATIC_USER_DB
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def read_user(username: str) -> UserBase:
    from config import config
    db = config.STATIC_USER_DB
    if username in db:
        user_dict = db[username]
        return UserBase(**user_dict)