from sqlmodel import  Session
from app.core.database import engine

class Repo:
    def __init__(self):
        self.session = Session(engine)