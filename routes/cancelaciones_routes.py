from typing import List
from fastapi import APIRouter, Depends
from requests import Session
from crud import cancelaciones_crud as crud
from schemas import cancelaciones_schema as schemas
from config.db import SessionLocal


cancelaciones_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@cancelaciones_routes.get("/cancelaciones", response_model=List[schemas.Cancelaciones])
def obtener_todas_las_cancelaciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_cancelaciones = crud.obtener_todas_las_cancelaciones(db=db, skip=skip, limit=limit)
    return db_cancelaciones
