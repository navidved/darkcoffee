from sqlmodel import SQLModel, create_engine, Session

from app.config import cfg


engine = create_engine(
    f"sqlite:///{cfg.APP_SETTING.SQLITE_DATABASE_PATH}")


def migrate() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> None:
    with Session(engine) as session:
        yield session
