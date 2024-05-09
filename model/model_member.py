import time

from sqlalchemy import String
from app import db

from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token

from sqlalchemy.orm import Mapped, mapped_column

class MemberModel(db.Model):
    __tablename__ = 'member'
    user_num: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[str] = mapped_column(String(20))
    pw: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(200),nullable=False)
    permit: Mapped[int] = mapped_column(nullable=False, default=0)
    create_at: Mapped[int] = mapped_column(nullable=False, default=time.time())
    update_at: Mapped[int] = mapped_column(nullable=True)