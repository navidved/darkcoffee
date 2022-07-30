from app.core.router import Router
import app.blog.routers.post_routes as post_routes
import app.blog.routers.user_routes as user_routes


class RouteTable(Router):
    Router.route_list = [
        post_routes.router,
        user_routes.router
    ]
