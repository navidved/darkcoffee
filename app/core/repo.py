from sqlmodel import Session
from app.core.database import Database


class Repo:
    def __init__(self):
        self.session = Session(Database().engine)
