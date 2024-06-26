from sqlalchemy import Column, Integer, String, Boolean, Date, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base
from .schemas import Gender

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    birth = Column(Integer)
    gender = Column(Enum(Gender))
    registration_date = Column(Date)
    consent = Column(Boolean)
    photo = Column(String, nullable=True)

    purchases = relationship("Purchase", back_populates="customer", cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    purchase_price = Column(Float)
    sale_price = Column(Float)

    purchase_items = relationship("PurchaseItem", back_populates="product", cascade="all, delete-orphan")


class PurchaseItem(Base):
    __tablename__ = "purchase_item"

    id = Column(Integer, primary_key=True, index=True)
    purchase_id = Column(Integer, ForeignKey("purchase.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer)
    price = Column(Float)
    total_price = Column(Float)

    purchase = relationship("Purchase", back_populates="items")
    product = relationship("Product", back_populates="purchase_items")


class Purchase(Base):
    __tablename__ = "purchase"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    purchase_date = Column(Date)

    customer = relationship("Customer", back_populates="purchases")
    items = relationship("PurchaseItem", back_populates="purchase", cascade="all, delete-orphan")
