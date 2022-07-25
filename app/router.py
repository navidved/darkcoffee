from fastapi import FastAPI
from app.core import root_routes
from app.blog.routers import post_routes, user_routes



class Router:
  def __init__(self, app: FastAPI):
    app.include_router(root_routes.router)
    app.include_router(post_routes.router)
    app.include_router(user_routes.router)
    

