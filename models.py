import os
from datetime import date, datetime

from sqlalchemy import DateTime, Date, MetaData, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

schema_name = os.getenv('PG_SCHEMA_NAME', 'app_schema')


class Base(DeclarativeBase):
    type_annotation_map = {
        datetime: DateTime(timezone=True),
        date: Date,
        dict: JSONB,
        list: JSONB
    }
    metadata = MetaData(schema=schema_name)


# ======= Start Writing Models Below =============


class Region(Base):
    __tablename__ = 'region'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    desc: Mapped[str] = mapped_column(nullable=False, unique=False)
    created: Mapped[datetime] = mapped_column(nullable=False, unique=False)
    updated: Mapped[datetime] = mapped_column(nullable=False, unique=False)
    houses: Mapped["House"] = relationship(back_populates="house")


class Faction(Base):
    __tablename__ = 'faction'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    desc: Mapped[str] = mapped_column(nullable=False, unique=False)
    created: Mapped[datetime] = mapped_column(nullable=False, unique=False)
    updated: Mapped[datetime] = mapped_column(nullable=False, unique=False)
    houses: Mapped["House"] = relationship(back_populates="house")


class House(Base):
    __tablename__ = "house"

    id: Mapped[int] = mapped_column(primary_key=True)
    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"), nullable=False)
    faction_id: Mapped[int] = mapped_column(ForeignKey("faction.id"), nullable=False)

    leader: Mapped[bool] = mapped_column(nullable=False)  # if they're a leader in a given region
    specialty: Mapped[str] = mapped_column(nullable=False)  # specialty fighting style
    created: Mapped[datetime] = mapped_column(nullable=False, unique=False)
    updated: Mapped[datetime] = mapped_column(nullable=False, unique=False)

    faction: Mapped["Faction"] = relationship(back_populates="faction")
    region: Mapped["Region"] = relationship(back_populates="region")


class Warrior(Base):
    __tablename__ = "warrior"

    id: Mapped[int] = mapped_column(primary_key=True)
    house_id: Mapped[int] = mapped_column(ForeignKey("house.id"), nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)  # warrior's name
    code: Mapped[str] = mapped_column(nullable=False)  # warrior code
    desc: Mapped[str] = mapped_column(nullable=False)  # text description of the warrior
    type: Mapped[str] = mapped_column(nullable=False)  # SWORDSMAN, ARCHER, CAVALRY
    status: Mapped[str] = mapped_column(nullable=False)  # APPROVED, DRAFT, IN_PROGRESS
    classification: Mapped[str] = mapped_column(nullable=False)  # STANDARD, NON-STANDARD

    house: Mapped["House"] = relationship(back_populates="house")