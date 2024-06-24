from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import Product, ProductUpdate, ProductCreate
from ..crud import products as crud 
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@router.get("/", response_model=List[Product])
def read_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return crud.update_product(db=db, product_id=product_id, product=product)

@router.delete("/{product_id}", response_model=Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db=db, product_id=product_id)
