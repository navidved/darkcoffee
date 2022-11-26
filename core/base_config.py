from os import path
from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    # App
    APP_NAME: str = "Darkcoffee"
    FAVICON_PATH: str = path.join("static", "favicon.ico")

    # Database
    # SQLLite
    SQLITE_DATABASE_NAME: str = "db.sqlite"
    SQLITE_DATABASE_PATH: str = "ds"

    # Security
    # generate random secret key => openssl rand -hex 32
    SECRET_KEY: str = "d560d0c0e505d36816042bffdefeb413f2703515ab778dbca7b68a1bf8adc054"
    PASS_HASHING_ALGORITHM: str = "bcrypt"
    JWT_ENCODE_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    AUTH_USER_METHOD: str = "get_user"
    AUTH_USER_MODULE: str = "core.user"
    AUTH_USER_HASSHED_PASS_FIELD: str = "hashed_password"
    AUTH_USER_DISABLED_FIELD: str = "disabled"
    STATIC_USER_DB = {
        "navid": {
            "username": "navid",
            "full_name": "Navid Ar.",
            "email": "navidved@gmail.com",
            # password = secret
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            "disabled": False,
        }
    }

    class Config:
        env_file = ".env"
