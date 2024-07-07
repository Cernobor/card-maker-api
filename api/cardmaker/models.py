"""
ORM models for 'Cardmaker' database and models for fastapi endpoints.
"""

from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    """
    Author of the card.
    Each Card instance has foreign key to User
    """

    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class CardType(SQLModel, table=True):
    """
    Type of card, which means for example Location or Magical item.
    Each Card has foreign key to CardType.
    """

    __tablename__ = "card_types"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class CardTagRelationship(SQLModel, table=True):
    """
    Link model for Card and Tag models.
    """

    __tablename__ = "cards_tags_relationship"

    card_id: int = Field(default=None, foreign_key="cards.id", primary_key=True)
    tag_id: int = Field(default=None, foreign_key="tags.id", primary_key=True)


class Card(SQLModel, table=True):
    """
    Main item of the app.
    Each Card instance has author (User) and type (CardType).
    """

    __tablename__ = "cards"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    fluff: Optional[str]
    effect: Optional[str]
    user_id: int = Field(foreign_key="users.id")
    card_type_id: int = Field(foreign_key="card_types.id")
    in_set: bool
    set_name: Optional[str]

    tags: list["Tag"] = Relationship(
        back_populates="cards", link_model=CardTagRelationship
    )


class Tag(SQLModel, table=True):
    """
    Tag, which can be attached to any Card instance.
    Tag can be anything, for example year of creation
    of something, which can help with filtering.
    """

    __tablename__ = "tags"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]

    cards: list[Card] = Relationship(
        back_populates="tags", link_model=CardTagRelationship
    )
