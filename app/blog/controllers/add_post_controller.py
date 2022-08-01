from app.blog.repository.post_repo import PostRepo
from app.blog.models.post_model import PostModel


def invoke(request: PostModel) -> PostModel:
    return PostRepo().add_post(request)
