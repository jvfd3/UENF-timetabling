""" Models """

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey

from database import Base


class Todo(Base):
    """ Todo Class """

    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    complete: Mapped[bool] = mapped_column(Boolean, default=False)


class Professor(Base):
    """ Professor Class """

    __tablename__ = "professor"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))


class Disciplina(Base):
    """ Disciplina Class"""

    __tablename__ = "disciplina"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    code: Mapped[str] = mapped_column(String(9))


class Turma(Base):
    """ Turma Class"""

    __tablename__ = "turma"

    id: Mapped[int] = mapped_column(primary_key=True)
    disciplina_id: Mapped[int] = mapped_column(ForeignKey("disciplina.id"))
    professor_id: Mapped[int] = mapped_column(ForeignKey("professor.id"))


class TimeSlot(Base):
    """ Timeslot Class"""

    __tablename__ = "time_slot"

    id: Mapped[int] = mapped_column(primary_key=True)
    turma_id: Mapped[int] = mapped_column(ForeignKey("turma.id"))
    slot: Mapped[int] = mapped_column(
        Integer
    )  # TODO: consider monA, tueC || AA, BC || 0, 10
