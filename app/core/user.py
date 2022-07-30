from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def get_user(username: str) -> UserInDB:
    import app.config as config
    db = config.cfg.APP_SETTING.FAKE_USER_DB
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
