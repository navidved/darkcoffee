
from fastapi import FastAPI
from . import root_routes


class Router(object):
    
    route_list: list = []

    base_route_list: list = [
        root_routes.router
    ]

    def __init__(self) -> None:
        self.route_list = self.base_route_list + self.route_list

    def render(self, app: FastAPI) -> None:
        list(map(app.include_router, self.route_list))
