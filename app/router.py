from fastapi import FastAPI
from app.core import root_router
from app.blog.routers import post_router, user_router



class Router:
  def __init__(self, app: FastAPI):
    app.include_router(root_router.router)
    app.include_router(post_router.router)
    app.include_router(user_router.router)
    

