from app.blog.repository.post_repo import PostRepo
from app.blog.models.post_model import PostModel
from typing import List


def invoke() -> List[PostModel]:
    return PostRepo().get_all_posts()
