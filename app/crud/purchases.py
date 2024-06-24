from sqlalchemy.orm import Session
from ..models import Purchase, PurchaseItem
from ..schemas import PurchaseCreate, PurchaseUpdate

def create_purchase(db: Session, purchase: PurchaseCreate):
    db_purchase = Purchase(customer_id=purchase.customer_id, purchase_date=purchase.purchase_date)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)

    for item in purchase.items:
        db_purchase_item = PurchaseItem(
            purchase_id=db_purchase.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
            total_price=item.quantity * item.price 
        )
        db.add(db_purchase_item)
    db.commit()
    return db_purchase

def get_purchase(db: Session, purchase_id: int):
    return db.query(Purchase).filter(Purchase.id == purchase_id).first()

def get_purchases(db: Session):
    return db.query(Purchase).all()

def update_purchase(db: Session, purchase_id: int, purchase: PurchaseUpdate):
    db_purchase = db.query(Purchase).filter(Purchase.id == purchase_id).first()
    if db_purchase:
        db.query(PurchaseItem).filter(PurchaseItem.purchase_id == purchase_id).delete()
        for key, value in purchase.dict(exclude_unset=True).items():
            if key != "items":
                setattr(db_purchase, key, value)
        db.commit()
        db.refresh(db_purchase)

        for item in purchase.items:
            db_purchase_item = PurchaseItem(
                purchase_id=db_purchase.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price,
                total_price=item.quantity * item.price
            )
            db.add(db_purchase_item)
        db.commit()
    return db_purchase

def delete_purchase(db: Session, purchase_id: int):
    db_purchase = db.query(Purchase).filter(Purchase.id == purchase_id).first()
    if db_purchase:
        db.query(PurchaseItem).filter(PurchaseItem.purchase_id == purchase_id).delete()
        db.delete(db_purchase)
        db.commit()
    return db_purchase
