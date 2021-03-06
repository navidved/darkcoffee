from fastapi import HTTPException
from sqlmodel import select
from app.core.repo import Repo
from app.blog.models.post_model import Post
from app.blog.schemes.post_schemes import PostBaseSchema



class PostRepo(Repo):

    def get_all_posts(self) -> list[Post]:
        statement = select(Post)
        posts = self.session.exec(statement).all()
        return posts

    def add_post(self, post: Post) -> Post:
        post.creator_user = 1
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post

    def show_post(self, id: int) -> Post:
        statement = select(Post).where(Post.id == id)
        post = self.session.exec(statement).first()
        return post

    def update_post(self, id: int, post_data: PostBaseSchema) -> Post:
        statement = select(Post).where(Post.id == id)
        results = self.session.exec(statement)
        current_post = results.first()

        current_post.title = post_data.title
        current_post.body = post_data.body

        self.session.add(current_post)
        self.session.commit()
        self.session.refresh(current_post)
        return current_post

    def delete_post(self, id: int) -> bool:
        post = self.session.get(Post, id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        self.session.delete(post)
        self.session.commit()
        return True
