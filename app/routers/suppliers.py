from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Supplier)
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    return crud.create_supplier(db, supplier)

@router.get("/", response_model=list[schemas.Supplier])
def list_suppliers(db: Session = Depends(get_db)):
    return crud.get_suppliers(db)

@router.put("/{supplier_id}", response_model=schemas.Supplier)
def update_supplier(supplier_id: int, supplier: schemas.SupplierUpdate, db: Session = Depends(get_db)):
    db_supplier = crud.update_supplier(db, supplier_id, supplier)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@router.delete("/{supplier_id}", response_model=schemas.Supplier)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = crud.delete_supplier(db, supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier