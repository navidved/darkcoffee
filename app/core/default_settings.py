from os import path, getcwd


class DefaultSettings:
    APP_NAME: str = "Darkcoffee"
    FAVICON_PATH: str = path.join("app", "static", "favicon.ico")

    # Database
    SQLITE_DATABASE_NAME: str = "sqlite.sqlite"
    SQLITE_DATABASE_DIR_PATH: str = path.join(
        path.abspath(getcwd()), "ds")
    SQLITE_DATABASE_PATH: str = ""

    # Security
    # generate random secret key => openssl rand -hex 32
    SECRET_KEY: str = "d560d0c0e505d36816042bffdefeb413f2703515ab778dbca7b68a1bf8adc054"
    PASS_HASHING_ALGORITHM: str = "bcrypt"
    JWT_ENCODE_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    GET_USER_METHOD: str = None
    FAKE_USER_DB = {
        "navid": {
            "username": "navid",
            "full_name": "Navid Ar.",
            "email": "navidved@gmail.com",
            # password = secret
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            "disabled": False,
        }
    }

    def __init__(self) -> None:
        self.set_db_name()
        self.set_user_method()

    def set_db_name(self, db_name: str = SQLITE_DATABASE_NAME) -> None:
        self.SQLITE_DATABASE_NAME = db_name
        self.SQLITE_DATABASE_PATH = path.join(
            self.SQLITE_DATABASE_DIR_PATH, self.SQLITE_DATABASE_NAME)

    def set_user_method(self) -> None:
        from app.core.user import get_user
        self.GET_USER_METHOD = get_user
