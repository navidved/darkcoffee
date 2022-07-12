from sqlmodel import SQLModel, create_engine, Session
from app.config import settings


engine = create_engine(f"sqlite:///{settings.sqlite_database_path}")


def migrate():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

