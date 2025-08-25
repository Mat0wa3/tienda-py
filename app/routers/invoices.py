from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/invoices", tags=["Invoices"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Invoice)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    return crud.create_invoice(db, invoice)

@router.get("/", response_model=list[schemas.Invoice])
def list_invoices(db: Session = Depends(get_db)):
    return crud.get_invoices(db)

@router.put("/{invoice_id}", response_model=schemas.Invoice)
def update_invoice(invoice_id: int, invoice: schemas.InvoiceUpdate, db: Session = Depends(get_db)):
    db_invoice = crud.update_invoice(db, invoice_id, invoice)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

@router.delete("/{invoice_id}", response_model=schemas.Invoice)
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = crud.delete_invoice(db, invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice