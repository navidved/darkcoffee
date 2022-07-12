from fastapi import FastAPI
from app.router import Router
from app.migration import Migration


app = FastAPI()
Migration()
Router(app)




