from app.core import database
from app.blog.models.post_model import Post
from app.blog.models.user_model import User


class Migration:
  def __init__(self):
    database.migrate()