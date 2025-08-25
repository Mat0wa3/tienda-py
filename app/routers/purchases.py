from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/purchases", tags=["Purchases"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Purchase)
def create_purchase(purchase: schemas.PurchaseCreate, db: Session = Depends(get_db)):
    return crud.create_purchase(db, purchase)

@router.get("/", response_model=list[schemas.Purchase])
def list_purchases(db: Session = Depends(get_db)):
    return crud.get_purchases(db)

@router.put("/{purchase_id}", response_model=schemas.Purchase)
def update_purchase(purchase_id: int, purchase: schemas.PurchaseUpdate, db: Session = Depends(get_db)):
    db_purchase = crud.update_purchase(db, purchase_id, purchase)
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return db_purchase

@router.delete("/{purchase_id}", response_model=schemas.Purchase)
def delete_purchase(purchase_id: int, db: Session = Depends(get_db)):
    db_purchase = crud.delete_purchase(db, purchase_id)
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return db_purchase