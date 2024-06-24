from fastapi import FastAPI
from .database import engine, Base
from sqlalchemy import inspect
from .routers import customers, products, purchases, report

def create_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    if 'customer' not in tables or 'product' not in tables or 'purchase' not in tables or 'purchase_item' not in tables:
        Base.metadata.create_all(bind=engine)

create_tables()

app = FastAPI(
    title="Simple CRUD app"
)

@app.get("/")
def read_root():
    return {"message": "OK!"}

app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(purchases.router, prefix="/purchases", tags=["purchases"])
app.include_router(report.router, prefix="/report", tags=["report"])
