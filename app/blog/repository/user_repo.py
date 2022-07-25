from sqlmodel import select
from app.blog.models.user_model import User
from app.blog.schemas import user_schemas
from fastapi import HTTPException, status
from app.core.hashing import Hash
from app.core.repo import Repo


class UserRepo(Repo):


  def add_user(self, request: user_schemas.User):
    new_user = User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    self.session.add(new_user)
    self.session.commit()
    self.session.refresh(new_user)
    return new_user


  def show_user(self, id: int):
    statement = select(User).where(User.id == id)
    user = self.session.exec(statement).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user


  def get_all_users(self):
    statement = select(User)
    users = self.session.exec(statement).all()
    return users