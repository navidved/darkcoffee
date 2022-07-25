from app.blog.repository.post_repo import PostRepo


def __invoke():
    return PostRepo().get_all_posts()