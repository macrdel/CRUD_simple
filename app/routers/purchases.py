from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import Purchase, PurchaseUpdate, PurchaseCreate
from ..crud import purchases as crud 
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=Purchase)
def create_purchase(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    return crud.create_purchase(db=db, purchase=purchase)

@router.get("/", response_model=List[Purchase])
def read_purchases(db: Session = Depends(get_db)):
    return crud.get_purchases(db)

@router.get("/{purchase_id}", response_model=Purchase)
def read_purchase(purchase_id: int, db: Session = Depends(get_db)):
    db_purchase = crud.get_purchase(db, purchase_id=purchase_id)
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return db_purchase

@router.put("/{purchase_id}", response_model=Purchase)
def update_purchase(purchase_id: int, purchase: PurchaseUpdate, db: Session = Depends(get_db)):
    return crud.update_purchase(db=db, purchase_id=purchase_id, purchase=purchase)

@router.delete("/{purchase_id}", response_model=Purchase)
def delete_purchase(purchase_id: int, db: Session = Depends(get_db)):
    return crud.delete_purchase(db=db, purchase_id=purchase_id)
