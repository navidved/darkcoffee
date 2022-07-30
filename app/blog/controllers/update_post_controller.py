from app.blog.repository.post_repo import PostRepo
from app.blog.schemes.post_schemes import PostBaseSchema
from app.blog.models.post_model import Post


def invoke(
    id: int,
    post_data: PostBaseSchema
) -> Post:
    return PostRepo().update_post(id, post_data)
