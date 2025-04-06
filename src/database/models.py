from typing import List, Optional
from dataclasses import dataclass

from sqlalchemy import Float, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import db
from src.database.associative import user_product_assoc

@dataclass
class Review(db.Model):
    __tablename__ = "reviews"

    id: Mapped[str] = mapped_column(String(), primary_key=True)
    text: Mapped[str] = mapped_column(String())
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))

@dataclass
class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    img_url: Mapped[str] = mapped_column(String)

    reviews: Mapped[List["Review"]] = relationship()
    users: Mapped[List["User"]] = relationship( secondary=user_product_assoc )

@dataclass 
class User(db.Model):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    