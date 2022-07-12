from app.blog import router as blog_router
from fastapi import FastAPI


class Router:
  def __init__(self, app: FastAPI):
    self.app = app
    self.tag = "Main"
    self.main_routes(self.app)
    app.include_router(blog_router.router)
    


  def main_routes(self, app: FastAPI):
    
    @app.get('/', tags=[self.tag])
    def root():
        return {"root"}


