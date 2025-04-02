from typing import List
from fastapi import APIRouter, Depends, HTTPException
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

@cancelaciones_routes.get("/cancelaciones/{id}", response_model=schemas.Cancelaciones)
def obtener_cancelaciones_por_ID(id: int, db: Session = Depends(get_db)):
    db_cancelaciones = crud.obtener_cancelaciones_por_ID(db=db, id=id)
    if db_cancelaciones is None:
        raise HTTPException(status_code=404, detail="La cancelación no existe")
    return db_cancelaciones

@cancelaciones_routes.get("/cancelaciones/usuario/{usuario_id}", response_model=List[schemas.Cancelaciones])
def obtener_cancelaciones_por_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_cancelaciones = crud.obtener_cancelaciones_por_usuario(db=db, usuario_solicitante=usuario_id)
    if db_cancelaciones is None:
        raise HTTPException(status_code=404, detail="No hay cancelaciones para este usuario")
    return db_cancelaciones


@cancelaciones_routes.get("/cancelaciones/citas/{cita_ID}", response_model=List[schemas.Cancelaciones])
def obtener_cancelaciones_por_cita(cita_ID: int, db: Session = Depends(get_db)):
    db_cancelaciones = crud.obtener_cancelaciones_por_cita(db=db, cita_ID=cita_ID)
    if db_cancelaciones is None:
        raise HTTPException(status_code=404, detail="No hay cancelaciones para esta cita")
    return db_cancelaciones

@cancelaciones_routes.post("/cancelaciones", response_model=schemas.Cancelaciones)
def crear_cancelaciones(cancelacion: schemas.CancelacionesCreate, db: Session = Depends(get_db)):
    db_cancelacion = crud.validar_cancelacion_existente(
        db=db,
        servicio_id=cancelacion.servicio_ID, 
        usuario_id=cancelacion.usuario_solicitante, 
        cita_id=cancelacion.cita_ID)
    
    if db_cancelacion:
        raise HTTPException(status_code=400, detail="La cancelación ya existe")
    return crud.crear_cancelaciones(db=db, cancelaciones=cancelacion)

@cancelaciones_routes.put("/cancelaciones/{id}", response_model=schemas.Cancelaciones)
def actualizar_cancelaciones(id: int, cancelacion: schemas.CancelacionesUpdate, db: Session = Depends(get_db)):
    db_cancelacion = crud.actualizar_cancelaciones(db=db, id=id, cancelaciones=cancelacion)
    if db_cancelacion is None:
        raise HTTPException(status_code=404, detail="La cancelación no existe")
    return db_cancelacion



@cancelaciones_routes.delete("/cancelaciones/{id}", response_model=schemas.Cancelaciones)
def eliminar_cancelaciones(id: int, db: Session = Depends(get_db)):
    db_cancelacion = crud.eliminar_cancelaciones(db=db, id=id)
    if db_cancelacion is None:
        raise HTTPException(status_code=404, detail="La cancelación no existe")
    return  db_cancelacion
