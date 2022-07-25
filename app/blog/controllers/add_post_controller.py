from app.blog.repository.post_repo import PostRepo
from app.blog.models import post_model


def __invoke(request: post_model.Post):
    return PostRepo().add_post(request)