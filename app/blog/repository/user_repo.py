from sqlmodel import select
from app.blog.models.user_model import UserModel, UserRead, UserPassUpdate, UserCreate, UserUpdate
from app.core.repo import Repo


class UserRepo(Repo):
    def add_user(self, user: UserCreate) -> UserRead:
        from app.core.hashing import get_password_hash

        db_user = UserModel.from_orm(user)
        db_user.hashed_password = get_password_hash(user.password)
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user


    def get_user(self, id: int) -> UserRead:
        return self.session.get(UserModel, id)


    def get_all_users(self, offset: int, limit: int) -> list[UserRead]:
        statement = select(UserModel).offset(offset).limit(limit)
        users = self.session.exec(statement).all()
        return users


    def update_user(self, id: int, user: UserUpdate) -> UserRead:
        db_user = self.session.get(UserModel, id)
        if not db_user:
            return None
        
        user_data = user.dict(exclude_unset=True)
        for key, value in user_data.items():
            setattr(db_user, key, value)
        
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user


    def delete_user(self, id: int) -> bool:
        user = self.session.get(UserModel, id)
        if not user:
            return False
        self.session.delete(user)
        self.session.commit()
        return True


    def get_user_by_username(self, username: str):
        statement = select(UserModel).where(UserModel.username == username)
        user = self.session.exec(statement).first()
        return user
