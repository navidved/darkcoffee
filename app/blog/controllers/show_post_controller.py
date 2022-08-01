from app.blog.repository.post_repo import PostRepo
from app.blog.models.post_model import PostModel


def invoke(id: int) -> PostModel:
    return PostRepo().show_post(id)