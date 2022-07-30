import app.core.root_routes as root_routes
import app.main as am 

class Router(object):
    route_list: list = []
    base_route_list: list = [
        root_routes.router
    ]

    def __init__(
        self
    ) -> None:
        self.route_list = self.base_route_list + self.route_list
        list(map(am.app.include_router, self.route_list))

