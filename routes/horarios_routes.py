from fastapi import APIRouter, Depends
from requests import Session
from config.db import SessionLocal
from crud import horarios_crud as crud
from schemas import horarios_schema as schemas
from typing import List


horarios_routes = APIRouter()  

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 

@horarios_routes.get("/horarios", response_model=List[schemas.Horarios])
def obtener_todos_los_horarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_horarios = crud.obtener_todos_los_horarios(db=db, skip=skip, limit=limit)
    return db_horarios