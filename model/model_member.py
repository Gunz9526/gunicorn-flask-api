import time

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app import db


class MemberModel(db.Model):
    __tablename__ = 'member'
    user_num: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[str] = mapped_column(String(20))
    password: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(200),nullable=False)
    permit: Mapped[int] = mapped_column(nullable=False, default=0)
    create_at: Mapped[int] = mapped_column(nullable=False, default=time.time())
    update_at: Mapped[int] = mapped_column(nullable=True)
    