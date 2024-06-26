import os
from typing import List
from datetime import date, datetime

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# ===== SQLAlchemy docs show creating the association table like this =====

association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("left_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
)


# ===== But this method works just fine =====

class Association(Base):
    __tablename__ = "association"
    id: Mapped[int] = mapped_column(primary_key=True)
    child_id = mapped_column(ForeignKey('children.id'), nullable=False)
    parent_id = mapped_column(ForeignKey('parents.id'), nullable=False)


class Parent(Base):
    __tablename__ = "parents"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List['Child']] = relationship(
        secondary='assoc', back_populates="parents"
    )


class Child(Base):
    __tablename__ = "children"

    id: Mapped[int] = mapped_column(primary_key=True)
    parents: Mapped[List['Parent']] = relationship(
        secondary='assoc', back_populates="children"
    )
