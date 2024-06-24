from sqlalchemy import Column, Integer, String, Boolean, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    birth = Column(Integer)
    gender = Column(String)
    registration_date = Column(Date)
    consent = Column(Boolean)
    photo = Column(String, nullable=True)

    purchases = relationship("Purchase", back_populates="customer")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    purchase_price = Column(Float)
    sale_price = Column(Float)

    purchase_items = relationship("PurchaseItem", back_populates="product")


class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id = Column(Integer, primary_key=True, index=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(Float)
    total_price = Column(Float)

    purchase = relationship("Purchase", back_populates="items")
    product = relationship("Product", back_populates="purchase_items")


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    purchase_date = Column(Date)

    customer = relationship("Customer", back_populates="purchases")
    items = relationship("PurchaseItem", back_populates="purchase")
