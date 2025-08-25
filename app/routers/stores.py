from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/stores", tags=["Stores"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Store)
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    return crud.create_store(db, store)

@router.get("/", response_model=list[schemas.Store])
def list_stores(db: Session = Depends(get_db)):
    return crud.get_stores(db)

# PUT: Actualizar una tienda
@router.put("/{store_id}", response_model=schemas.Store)
def update_store(store_id: int, store: schemas.StoreUpdate, db: Session = Depends(get_db)):
    db_store = crud.update_store(db, store_id, store)
    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return db_store

# DELETE: Eliminar una tienda
@router.delete("/{store_id}", response_model=schemas.Store)
def delete_store(store_id: int, db: Session = Depends(get_db)):
    db_store = crud.delete_store(db, store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return db_store