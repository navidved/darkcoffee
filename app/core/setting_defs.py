from pydantic import BaseSettings
from os import path, getcwd


class SettingDefs(BaseSettings):   
    app_name: str = "Darkcoffee" 
    sqlite_database_name: str = "sqlite.db"
    sqlite_database_path: str = path.join(path.abspath(getcwd()) ,"ds", sqlite_database_name)
