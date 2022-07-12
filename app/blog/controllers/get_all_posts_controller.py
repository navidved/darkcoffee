from app.blog.repository import post_repo


def __invoke():
    return post_repo.get_all_posts()