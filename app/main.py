from fastapi import FastAPI
from app.database import Base, engine
from app.routers import stores, employees, customers, suppliers, purchases, invoices

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API para Cadena de Tiendas")

app.include_router(stores.router)
app.include_router(employees.router)
app.include_router(customers.router)
app.include_router(suppliers.router)
app.include_router(purchases.router)
app.include_router(invoices.router)
