from app.blog.repository.post_repo import PostRepo
from app.blog.schemes.post_schemes import PostBaseSchema
from app.blog.models.post_model import PostModel


def invoke(
    id: int,
    post_data: PostBaseSchema
) -> PostModel:
    return PostRepo().update_post(id, post_data)
