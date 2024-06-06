import time
from app import db

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class CommentModel(db.Model):
    __tablename__ = 'comment'
    comment_num: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[str] = mapped_column(nullable=False)
    board_num: Mapped[int] = mapped_column(nullable=False)
    nested: Mapped[int] = mapped_column(nullable=True, default=0)
    regdate: Mapped[int] = mapped_column(nullable=False, default=time.time())