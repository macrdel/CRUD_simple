from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class CustomerBase(BaseModel):
    name: str
    birth: int
    gender: Gender
    registration_date: date
    consent: bool
    photo: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    purchase_price: float
    sale_price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class PurchaseItemBase(BaseModel):
    purchase_id: int
    product_id: int
    quantity: int
    price: float
    total_price: float

class PurchaseItemCreate(PurchaseItemBase):
    pass

class PurchaseItemUpdate(PurchaseItemBase):
    pass

class PurchaseItem(PurchaseItemBase):
    id: int

    class Config:
        orm_mode = True

class PurchaseBase(BaseModel):
    customer_id: int
    purchase_date: date

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseUpdate(PurchaseBase):
    pass

class Purchase(PurchaseBase):
    id: int
    items: List[PurchaseItem]

    class Config:
        orm_mode = True
