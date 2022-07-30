from app.blog.repository.post_repo import PostRepo
from app.blog.models.post_model import Post


def invoke(id: int) -> Post:
    return PostRepo().show_post(id)