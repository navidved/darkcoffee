from pydantic import BaseSettings
from app.core.default_settings import DefaultSettings


class Config(BaseSettings):
    # define custom apps settings
    EMAIL: str = "navidved@gmail.com"
    MODEL_PATH: str = ""
    # change default setting
    APP_SETTING: DefaultSettings = DefaultSettings()
    APP_SETTING.APP_NAME = "DRKApp"
    APP_SETTING.SQLITE_DATABASE_NAME = "blog.db"
    APP_SETTING.rest_db_path()


def set_user_method(cfg: Config):
    from app.blog.repository.user_repo import UserRepo
    cfg.APP_SETTING.GET_USER_METHOD = UserRepo().get_db_user


cfg = Config()
set_user_method(cfg)
