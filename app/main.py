from fastapi import FastAPI
from app.route_table import RouteTable
import app.models_order 

app = FastAPI()
RouteTable()



