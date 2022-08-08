from fastapi import HTTPException
from sqlmodel import select
from app.core.repo import Repo
from app.blog.models.post_model import PostModel
from app.blog.schemes.post_schemes import PostBaseSchema



class PostRepo(Repo):

    def get_all_posts(self) -> list[PostModel]:
        statement = select(PostModel)
        posts = self.session.exec(statement).all()
        return posts

    def add_post(self, post: PostModel) -> PostModel:
        post.creator_user = 1
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post

    def get_post(self, id: int) -> PostModel:
        statement = select(PostModel).where(PostModel.id == id)
        post = self.session.exec(statement).first()
        return post

    def update_post(self, id: int, post_data: PostBaseSchema) -> PostModel:
        statement = select(PostModel).where(PostModel.id == id)
        results = self.session.exec(statement)
        current_post = results.first()

        current_post.title = post_data.title
        current_post.body = post_data.body

        self.session.add(current_post)
        self.session.commit()
        self.session.refresh(current_post)
        return current_post

    def delete_post(self, id: int) -> bool:
        post = self.session.get(PostModel, id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        self.session.delete(post)
        self.session.commit()
        return True
