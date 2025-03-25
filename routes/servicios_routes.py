from typing import List
from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from config.db import SessionLocal
from crud import servicios_crud as crud
from schemas import servicios_schema as schemas


servicios_routes = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@servicios_routes.get("/servicios", response_model=List[schemas.Servicios])
def obtener_todos_los_servicios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_servicios = crud.obtener_todos_los_servicios(db=db, skip=skip, limit=limit)
    return db_servicios

@servicios_routes.get("/servicios/{id}", response_model=schemas.Servicios)
def obtener_servicios_por_ID(id: int, db: Session = Depends(get_db)):
    db_servicios = crud.obtener_servicios_por_ID(db=db, id=id)
    if db_servicios is None:
        raise HTTPException(status_code=404, detail="El servicio no existe")
    return db_servicios

@servicios_routes.post("/servicios", response_model=schemas.Servicios)
def crear_servicios(servicio: schemas.ServiciosCreate, db: Session = Depends(get_db)):
    db_servicios = crud.validar_servicio_existente(db=db, nombre=servicio.nombre, sucursal_id=servicio.sucursal_id)
    if db_servicios:
        raise HTTPException(status_code=400, detail="El servicio ya existe")
    return crud.crear_servicios(db=db, servicios=servicio)

@servicios_routes.put("/servicios/{id}", response_model=schemas.Servicios)
def actualizar_servicios(id: int, personas: schemas.ServiciosUpdate, db: Session = Depends(get_db)):
    db_servicios = crud.actualizar_servicios(db=db, id=id, personas=personas)
    if db_servicios is None:
        raise HTTPException(status_code=404, detail="El servicio no existe")
    return db_servicios

@servicios_routes.delete("/servicios/{id}", response_model=schemas.Servicios)
def eliminar_servicios(id: int, db: Session = Depends(get_db)):
    db_servicios = crud.eliminar_servicios(db=db, id=id)
    if db_servicios is None:
        raise HTTPException(status_code=404, detail="El servicios no existe")
    return  db_servicios

