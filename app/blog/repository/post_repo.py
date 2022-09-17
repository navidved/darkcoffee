from sqlmodel import select
from app.core.repo import Repo
from app.blog.models.post_model import PostCreate, PostModel, PostRead, PostUpdate
from app.core.user import User



class PostRepo(Repo):
    def add_post(
        self,
        post: PostCreate,
        current_user: User
    ) -> PostRead:
        db_post = PostModel.from_orm(post)
        db_post.author_id = current_user.id
        self.session.add(db_post)
        self.session.commit()
        self.session.refresh(db_post)
        return db_post


    def get_all_posts(self, offset: int, limit: int) -> list[PostRead]:
        statement = select(PostModel).offset(offset).limit(limit)
        posts = self.session.exec(statement).all()
        return posts


    def get_post(self, id: int) -> PostRead:
        return self.session.get(PostModel, id)


    def update_post(self, id: int, post: PostUpdate) -> PostRead:
        db_post = self.session.get(PostModel, id)
        if not db_post:
            return None

        post_data = post.dict(exclude_unset=True)
        for key, value in post_data.items():
            setattr(db_post, key, value)

        self.session.add(db_post)
        self.session.commit()
        self.session.refresh(db_post)
        return db_post


    def delete_post(self, id: int) -> bool:
        post = self.session.get(PostModel, id)
        if not post:
            return False
        self.session.delete(post)
        self.session.commit()
        return True
