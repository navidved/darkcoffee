from fastapi import FastAPI
from app.router import Router

app = FastAPI()
Router(app)

