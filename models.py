import os
from typing import List
from datetime import date, datetime

from sqlalchemy import DateTime, Date, MetaData, ForeignKey, Table, Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

schema_name = os.getenv('PG_SCHEMA_NAME', 'public')


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

# class House(Base):
#     __tablename__ = 'houses'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'), nullable=False)
#     faction_id: Mapped[int] = mapped_column(ForeignKey('factions.id'), nullable=False)
#
#     leader: Mapped[bool] = mapped_column(nullable=False)  # if they're a leader in a given region
#     specialty: Mapped[str] = mapped_column(nullable=False)  # specialty fighting style
#     created: Mapped[datetime] = mapped_column(nullable=False, unique=False)
#     updated: Mapped[datetime] = mapped_column(nullable=False, unique=False)

# association_table = Table(
#     "houses",
#     Base.metadata,
#     Column("region_id", ForeignKey("regions.id"), primary_key=True),
#     Column("faction_id", ForeignKey("factions.id"), primary_key=True),
# )
#
#
# class Region(Base):
#     __tablename__ = 'regions'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     code: Mapped[str] = mapped_column(nullable=False, unique=True)
#     name: Mapped[str] = mapped_column(nullable=False, unique=True)
#     desc: Mapped[str] = mapped_column(nullable=False, unique=False)
#     created: Mapped[datetime] = mapped_column(nullable=False, unique=False)
#     updated: Mapped[datetime] = mapped_column(nullable=False, unique=False)
#     factions: Mapped[List['Faction']] = relationship(secondary='houses', back_populates='factions')
#
#
# class Faction(Base):
#     __tablename__ = 'factions'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     code: Mapped[str] = mapped_column(nullable=False, unique=True)
#     name: Mapped[str] = mapped_column(nullable=False, unique=True)
#     desc: Mapped[str] = mapped_column(nullable=False, unique=False)
#     created: Mapped[datetime] = mapped_column(nullable=False, unique=False)
#     updated: Mapped[datetime] = mapped_column(nullable=False, unique=False)
#     regions: Mapped[List['Region']] = relationship(secondary='houses', back_populates='regions')



    # faction: Mapped['Faction'] = relationship(back_populates='faction')
    # region: Mapped['Region'] = relationship(back_populates='region')


# class Warrior(Base):
#     __tablename__ = 'warrior'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     house_id: Mapped[int] = mapped_column(ForeignKey('house.id'), nullable=False)
#
#     name: Mapped[str] = mapped_column(nullable=False)  # warrior's name
#     code: Mapped[str] = mapped_column(nullable=False)  # warrior code
#     desc: Mapped[str] = mapped_column(nullable=False)  # text description of the warrior
#     type: Mapped[str] = mapped_column(nullable=False)  # SWORDSMAN, ARCHER, CAVALRY
#     status: Mapped[str] = mapped_column(nullable=False)  # APPROVED, DRAFT, IN_PROGRESS
#     classification: Mapped[str] = mapped_column(nullable=False)  # STANDARD, NON-STANDAR
#     D
from datetime import datetime

date_now = datetime.now()

# association_table2 = Table(
#     "association_table2",
#     Base.metadata,
#     Column("left_id", ForeignKey("left_table.id"), primary_key=True),
#     Column("right_id", ForeignKey("right_table.id"), primary_key=True),
# )


class Association(Base):
    __tablename__ = "assoc"
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


class House(Base):
    __tablename__ = "houses"
    id: Mapped[int] = mapped_column(primary_key=True)
    region_id = mapped_column(ForeignKey('regions.id'), nullable=False)
    faction_id = mapped_column(ForeignKey('factions.id'), nullable=False)
    # leader: Mapped[bool] = mapped_column(nullable=False)  # if they're a leader in a given region
    specialty: Mapped[str] = mapped_column(nullable=False)  # specialty fighting style


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

