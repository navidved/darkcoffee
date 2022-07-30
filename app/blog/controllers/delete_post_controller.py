from app.blog.repository.post_repo import PostRepo


def invoke(id: int) -> bool:
    return PostRepo().delete_post(id)
