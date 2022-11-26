from core.router import Router
import services.game.routes.team_routes as team_routes
import services.game.routes.hero_routes as hero_routes
import services.blog.routes.agent_routes as agent_routes
import services.blog.routes.post_routes as post_routes


class RouteTable(Router):
    route_list = [
        team_routes.router,
        hero_routes.router,
        agent_routes.router,
        post_routes.router
    ]
