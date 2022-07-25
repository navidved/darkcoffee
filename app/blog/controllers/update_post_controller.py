from app.blog.repository.post_repo import PostRepo
from app.blog.schemes import post_schemes


def __invoke(id:int, post_data: post_schemes.PostBase):
    return PostRepo().update_post(id, post_data)