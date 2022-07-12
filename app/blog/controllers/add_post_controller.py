from app.blog.repository import post_repo
from app.blog.models import post_model


def __invoke(request: post_model.Post):
    return post_repo.add_post(request)