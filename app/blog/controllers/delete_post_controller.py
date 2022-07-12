from app.blog.repository import post_repo


def __invoke(id: int):
    return post_repo.delete_post(id)