from typing import List
from fastapi import APIRouter, Depends
from requests import Session
from config.db import SessionLocal
from schemas import promociones_schema as schemas
from crud import promociones_crud as crud


promociones_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@promociones_routes.get("/promociones", response_model=List[schemas.Promociones])
def obtener_todas_las_promociones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_promociones = crud.obtener_todas_las_promociones(db=db, skip=skip, limit=limit)
    return db_promociones