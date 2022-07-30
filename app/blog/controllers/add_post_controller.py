from app.blog.repository.post_repo import PostRepo
from app.blog.models.post_model import Post


def invoke(request: Post) -> Post:
    return PostRepo().add_post(request)
