from pydantic import BaseSettings
from app.core.default_settings import DefaultSettings


class Config(BaseSettings):
    # define custom apps settings
    EMAIL: str = "navidved@gmail.com"
    MODEL_NAME: str = "nlp_model"
    
    # change default setting
    APP_SETTING = DefaultSettings()
    APP_SETTING.APP_NAME = "DC-App"
    APP_SETTING.set_db_name("db.sqlite")


def set_user_method(cfg: Config):
    from app.blog.repository.user_repo import UserRepo
    cfg.APP_SETTING.GET_USER_METHOD = UserRepo().get_user_by_username


cfg = Config()
set_user_method(cfg)
