from app.blog.repository.post_repo import PostRepo


def __invoke(id: int):
    return PostRepo().show_post(id)