from os import path, getcwd


class DefSettings():
    def __init__(self):
        # App Settings
        self.APP_NAME: str = "Darkcoffee"

        # Database
        self.SQLITE_DATABASE_NAME: str = "sqlite.db"
        self.SQLITE_DATABASE_DIR_PATH: str = path.join(
            path.abspath(getcwd()), "ds")
        self.SQLITE_DATABASE_PATH: str = path.join(
            self.SQLITE_DATABASE_DIR_PATH, self.SQLITE_DATABASE_NAME)

        # Security
        self.SECRET_KEY = "761897f317db6a1650151757f4331fefb8555c9519df6d27778c212534195706"
        self.HASHING_ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30

        # Set Dynamic Variables
    def refresh_db_path(self):
        self.SQLITE_DATABASE_PATH: str = path.join(
            self.SQLITE_DATABASE_DIR_PATH, self.SQLITE_DATABASE_NAME)
