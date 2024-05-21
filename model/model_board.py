import time
from app import db

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped


class BoardModel(db.Model):
    __tablename__ = 'board'
    board_num: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(String(1000))
    board_type: Mapped[int] = mapped_column(nullable=False, default=0)
    regdate: Mapped[int] = mapped_column(nullable=False, default=time.time())
    writer: Mapped[int] = mapped_column(nullable=False)
