from typing import List
from fastapi import APIRouter, Depends, HTTPException
from config.db import SessionLocal
from sqlalchemy.orm import Session
from crud import direcciones_crud as crud
from schemas import direcciones_schema as schemas
from services.portador_token import Portador


direcciones_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@direcciones_routes.get("/direcciones", response_model=List[schemas.Direcciones], dependencies=[Depends(Portador())])
def obtener_todas_las_direcciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_direcciones = crud.obtener_todas_las_direcciones(db=db, skip=skip, limit=limit)
    return db_direcciones

@direcciones_routes.get("/direcciones/{id}", response_model=schemas.Direcciones)
def obtener_direcciones_por_ID(id: int, db: Session = Depends(get_db)):
    db_direcciones = crud.obtener_direcciones_por_ID(db=db, id=id)
    if db_direcciones is None:
        raise HTTPException(status_code=404, detail="La dirección no existe")
    return db_direcciones

@direcciones_routes.post("/direcciones", response_model=schemas.Direcciones)
def crear_direcciones(direcciones: schemas.DireccionesCreate, db: Session = Depends(get_db)):
    db_direcciones = crud.obtener_direcciones_por_ID(db=db, id=direcciones.id)
    if db_direcciones:
        raise HTTPException(status_code=400, detail="La dirección ya existe")
    return crud.crear_direcciones(db=db, direcciones=direcciones)

@direcciones_routes.put("/direcciones/{id}", response_model=schemas.Direcciones)
def actualizar_direcciones(id: int, direcciones: schemas.DireccionesUpdate, db: Session = Depends(get_db)):
    db_direcciones = crud.actualizar_direcciones(db=db, id=id, direcciones=direcciones)
    if db_direcciones is None:
        raise HTTPException(status_code=404, detail="La dirección no existe")
    return db_direcciones

@direcciones_routes.delete("/direcciones/{id}", response_model=schemas.Direcciones)
def eliminar_direcciones(id: int, db: Session = Depends(get_db)):
    db_direcciones = crud.eliminar_direcciones(db=db, id=id)
    if db_direcciones is None:
        raise HTTPException(status_code=404, detail="La dirección no existe")
    return  db_direcciones