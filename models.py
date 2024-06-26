import os
from typing import List
from datetime import date, datetime

from sqlalchemy import DateTime, Date, MetaData, ForeignKey, Table, Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

schema_name = os.getenv('PG_SCHEMA_NAME', 'public')

date_now = datetime.now()


class Base(DeclarativeBase):
    pass
    # type_annotation_map = {
    #     datetime: DateTime(timezone=True),
    #     date: Date,
    #     dict: JSONB,
    #     list: JSONB
    # }
    # metadata = MetaData()


# ======= Start Writing Models Below =============

'''
A house belonging to a faction will be established within a region. 
Warriors are associated with each house.

'''


class House(Base):
    __tablename__ = "houses"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    desc: Mapped[str] = mapped_column(nullable=False, unique=False)

    region_id = mapped_column(ForeignKey('regions.id'), nullable=False)
    faction_id = mapped_column(ForeignKey('factions.id'), nullable=False)
    # leader: Mapped[bool] = mapped_column(nullable=False)  # if they're a leader in a given region
    # specialty: Mapped[str] = mapped_column(nullable=False)  # specialty fighting style


class Region(Base):
    __tablename__ = "regions"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    desc: Mapped[str] = mapped_column(nullable=False, unique=False)

    factions: Mapped[List['Faction']] = relationship(
        secondary='houses', back_populates="regions"
    )


class Faction(Base):
    __tablename__ = "factions"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    desc: Mapped[str] = mapped_column(nullable=False, unique=False)

    regions: Mapped[List['Region']] = relationship(
        secondary='houses', back_populates="factions"
    )


class Warrior(Base):
    __tablename__ = 'warrior'

    id: Mapped[int] = mapped_column(primary_key=True)
    house_id: Mapped[int] = mapped_column(ForeignKey('houses.id'), nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)  # warrior's name
    code: Mapped[str] = mapped_column(nullable=False)  # warrior code
    desc: Mapped[str] = mapped_column(nullable=False)  # text description of the warrior
    type: Mapped[str] = mapped_column(nullable=False)  # SWORDSMAN, ARCHER, CAVALRY

