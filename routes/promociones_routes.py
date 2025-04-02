from typing import List
from fastapi import APIRouter, Depends, HTTPException
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

@promociones_routes.get("/promociones/{id}", response_model=schemas.Promociones)
def obtener_promociones_por_ID(id: int, db: Session = Depends(get_db)):
    db_promociones = crud.obtener_promociones_por_ID(db=db, id=id)
    if db_promociones is None:
        raise HTTPException(status_code=404, detail="La promoción no existe")
    return db_promociones

@promociones_routes.post("/promociones", response_model=schemas.Promociones)
def crear_promociones(promociones: schemas.PromocionesCreate, db: Session = Depends(get_db)):
    db_promociones = crud.existe_promocion(db=db, titulo=promociones.titulo, servico_id=promociones.servicio_ID)
    if db_promociones:
        raise HTTPException(status_code=400, detail="La promoción ya existe")
    return crud.crear_promociones(db=db, promociones=promociones)

@promociones_routes.put("/promociones/{id}", response_model=schemas.Promociones)
def actualizar_promociones(id: int, promociones: schemas.PromocionesUpdate, db: Session = Depends(get_db)):
    db_promociones = crud.actualizar_promociones(db=db, id=id, promociones=promociones)
    if db_promociones is None:
        raise HTTPException(status_code=404, detail="La promoción no existe")
    return db_promociones

@promociones_routes.delete("/promociones/{id}", response_model=schemas.Promociones)
def eliminar_promociones(id: int, db: Session = Depends(get_db)):   
    db_promociones = crud.eliminar_promociones(db=db, id=id)
    if db_promociones is None:
        raise HTTPException(status_code=404, detail="La promoción no existe")
    return  db_promociones




