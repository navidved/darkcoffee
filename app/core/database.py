from sqlmodel import SQLModel, create_engine, Session
from app.config import cfg


class Database:
    def __init__(self) -> None:
        self.engine = create_engine(
            f"sqlite:///{cfg.APP_SETTING.SQLITE_DATABASE_PATH}")

    def migrate(self) -> None:
        SQLModel.metadata.create_all(self.engine)

    def get_session(self) -> None:
        with Session(self.engine) as session:
            yield session
