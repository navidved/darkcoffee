from app.core.router import Router
import app.blog.routers.post_routes as post_routes
import app.blog.routers.user_routes as user_routes
import app.blog.routers.hero_routes as hero_routes
import app.blog.routers.team_routes as team_routes


class RouteTable(Router):
    Router.route_list = [
        post_routes.router,
        user_routes.router,
        hero_routes.router,
        team_routes.router
    ]
