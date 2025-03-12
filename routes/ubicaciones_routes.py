from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from typing import List
from config.db import SessionLocal
from crud import ubicaciones_crud as crud
from schemas import ubicaciones_schema as schemas
from config.db import SessionLocal


ubicaciones_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@ubicaciones_router.get("/ubicaciones", response_model=List[schemas.Ubicaciones])
def obtener_todas_las_ubicaciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_ubicaciones = crud.obtener_todas_las_ubicaciones(db=db, skip=skip, limit=limit)
    return db_ubicaciones
