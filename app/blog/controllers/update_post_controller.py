from app.blog.repository.post_repo import PostRepo
from app.blog.schemas import post_schemas


def __invoke(id:int, post_data: post_schemas.PostBase):
    return PostRepo().update_post(id, post_data)