from pydantic import BaseSettings
from os import path
from app.core.def_settings import DefSettings


class Settings(BaseSettings):
    # define app settings
    EMAIL: str = "navidved@gmail.com"
    COMPANY: str = "AlphaNeuron"

    # customize defult app settings
    class AppConfig(DefSettings):
        def __init__(self):
            super().__init__()
            self.APP_NAME = "Navid App"
            self.SQLITE_DATABASE_NAME = "blog.db"
            self.refresh_db_path()


settings = Settings()
