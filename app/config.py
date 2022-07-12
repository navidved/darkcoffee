import imp
from pydantic import BaseSettings
import sqlalchemy
from os import path, getcwd


class Settings(BaseSettings):
    app_name: str = "DarkCoffee Blog"
    email: str = "navidved@gmail.com"
    sqlite_database_name: str = "blog.db"
    sqlite_database_path: str = path.join(path.abspath(getcwd()) ,"ds", sqlite_database_name)

settings = Settings()