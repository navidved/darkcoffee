from app.blog.models.post_model import Post
from sqlmodel import select, Session
from app.core.database import engine
from app.blog import schemas
from fastapi import FastAPI, HTTPException, Query


def get_all_posts():
    with Session(engine) as session:
        statement = select(Post)
        posts = session.exec(statement).all()
        return posts


def add_post(post: Post):
    with Session(engine) as session:
        session.add(post)
        session.commit()
        session.refresh(post)
        return post


def show_post(id: int):
    with Session(engine) as session:
        statement = select(Post).where(Post.id == id)
        post = session.exec(statement).one()
        return post


def update_post(id: int, post_data: schemas.PostBase):
    with Session(engine) as session:
        statement = select(Post).where(Post.id == id)
        results = session.exec(statement)  
        current_post = results.one()  

        current_post.title = post_data.title
        current_post.body = post_data.body

        session.add(current_post)  
        session.commit()  
        session.refresh(current_post)
        return current_post


def delete_post(id: int):
    with Session(engine) as session:
        post = session.get(Post, id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        session.delete(post)
        session.commit()
        return {"done!": True}