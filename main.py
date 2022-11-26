from fastapi import FastAPI
from route_table import RouteTable
import models_order


app = FastAPI()
RouteTable().render(app)
