from fastapi import APIRouter, Depends
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
