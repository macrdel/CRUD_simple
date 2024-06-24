from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from ..src.report import get_report, Report
from ..dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[Report])
def get_report(purchase_date: date, db: Session = Depends(get_db)):
    return get_report(db=db, purchase_date=purchase_date)
