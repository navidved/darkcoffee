from app.blog.repository import post_repo
from app.blog import schemas


def __invoke(id:int, post_data: schemas.PostBase):
    return post_repo.update_post(id, post_data)