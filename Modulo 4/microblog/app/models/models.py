from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    remember: Mapped[bool] = mapped_column(default=False)
    last_login: Mapped[datetime] = mapped_column(nullable=False)
    foto: Mapped[Optional[str]] = mapped_column(default='')
    bio: Mapped[Optional[str]] = mapped_column(default='')
    posts: Mapped[list['Post']] = relationship(back_populates='author')

class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    body: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    author: Mapped[User] = relationship(back_populates='posts')