""" Models """

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database import Base


class Todo(Base):
    """ Todo Class """
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    complete: Mapped[bool] = mapped_column(Boolean, default=False)
# schemas?
