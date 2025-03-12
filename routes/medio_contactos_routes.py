from typing import List
from fastapi import APIRouter, Depends
from requests import Session
from crud import medio_contactos_crud as crud
from schemas import medio_contactos_schema as schemas
from config.db import SessionLocal


medio_contactos_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@medio_contactos_router.get("/medio_contactos", response_model=List[schemas.MedioContactos])  
def obtener_todos_los_medios_contactos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_medio_contactos = crud.obtener_todos_medios_contactos(db=db, skip=skip, limit=limit)
    return db_medio_contactos