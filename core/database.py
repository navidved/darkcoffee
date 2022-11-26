from os import path, getcwd
from sqlmodel import SQLModel, create_engine, Session

from config import config
from .singleton_class import SingletonClass


class Database(metaclass=SingletonClass):
    def __init__(self) -> None:
        sqlite_file_full_path = path.join(path.abspath(
            getcwd()), config.SQLITE_DATABASE_PATH, config.SQLITE_DATABASE_NAME)
        sqlite_url = f"sqlite:///{sqlite_file_full_path}"
        self.engine = create_engine(sqlite_url)

    def migrate(self) -> None:
        SQLModel.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        with Session(self.engine) as session:
            return session

    async def get_session_depend(self) -> Session:
        with Session(self.engine) as session:
            yield session

