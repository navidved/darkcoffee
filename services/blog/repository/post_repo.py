from sqlmodel import select

from core.database import Database
from services.blog.models.post_model import PostCreate, PostModel, PostRead, PostUpdate
from services.blog.models.agent_model import AgentRead


class PostRepo():
    def add_post(
        self,
        post: PostCreate,
        current_user: AgentRead
    ) -> PostRead:
        db_post = PostModel.from_orm(post)
        db_post.author_id = current_user.id
        session = Database().get_session()
        session.add(db_post)
        session.commit()
        session.refresh(db_post)
        return db_post

    def get_all_posts(self, offset: int, limit: int) -> list[PostRead]:
        statement = select(PostModel).offset(offset).limit(limit)
        session = Database().get_session()
        posts = session.exec(statement).all()
        return posts

    def get_post(self, id: int) -> PostRead:
        session = Database().get_session()
        return session.get(PostModel, id)

    def update_post(self, id: int, post: PostUpdate) -> PostRead:
        session = Database().get_session()
        db_post = session.get(PostModel, id)
        if not db_post:
            return None

        post_data = post.dict(exclude_unset=True)
        for key, value in post_data.items():
            setattr(db_post, key, value)

        session.add(db_post)
        session.commit()
        session.refresh(db_post)
        return db_post

    def delete_post(self, id: int) -> bool:
        session = Database().get_session()
        post = session.get(PostModel, id)
        if not post:
            return False
        session.delete(post)
        session.commit()
        return True
