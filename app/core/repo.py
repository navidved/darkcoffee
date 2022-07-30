from sqlmodel import  Session

import app.core.database as db

class Repo:
    def __init__(self):
        self.session = Session(db.engine)