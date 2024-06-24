from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from datetime import date
from ..models import Customer, Purchase, PurchaseItem 

class Report(BaseModel):
    customer_id: int
    customer_name: str
    total_sum: float

def get_report(db: Session, purchase_date: date):
    report = (db.query(
        Customer.id.label('customer_id'),
        Customer.name.label('customer_name'),
        func.sum(PurchaseItem.total_price).label('total_sum')
    ).join(Purchase).join(PurchaseItem)\
     .filter(Purchase.purchase_date == purchase_date)\
     .group_by(Customer.id)\
     .order_by(func.sum(PurchaseItem.total_price).desc())\
     .all())
    return report