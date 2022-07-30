from app.blog.repository.post_repo import PostRepo
from app.blog.models.post_model import Post


def invoke() -> list[Post]:
    return PostRepo().get_all_posts()
