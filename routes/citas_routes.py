from typing import List
from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from crud import citas_crud as crud
from schemas import citas_schema as schemas
from config.db import SessionLocal


citas_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@citas_routes.get("/citas", response_model=List[schemas.Citas])
def obtener_todas_las_citas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_citas = crud.obtener_todas_las_citas(db=db, skip=skip, limit=limit)
    return db_citas


@citas_routes.get("/citas/{id}", response_model=schemas.Citas)
def obtener_citas_por_ID(id: int, db: Session = Depends(get_db)):
    db_citas = crud.obtener_citas_por_ID(db=db, id=id)
    if db_citas is None:
        raise HTTPException(status_code=404, detail="La cita no existe")
    return db_citas

@citas_routes.post("/citas", response_model=schemas.Citas)
def crear_citas(citas: schemas.CitasCreate, db: Session = Depends(get_db)):
    db_citas = crud.obtener_citas_por_ID(db=db, id=citas.id)
    if db_citas:
        raise HTTPException(status_code=400, detail="La cita ya existe")
    return crud.crear_cita(db=db, citas=citas)

@citas_routes.put("/citas/{id}", response_model=schemas.Citas)
def actualizar_citas(id: int, citas: schemas.CitasUpdate, db: Session = Depends(get_db)):
    db_citas = crud.actualizar_citas(db=db, id=id, citas=citas)
    if db_citas is None:
        raise HTTPException(status_code=404, detail="La cita no existe")
    return db_citas

@citas_routes.delete("/citas/{id}", response_model=schemas.Citas)
def eliminar_citas(id: int, db: Session = Depends(get_db)):
    db_citas = crud.eliminar_citas(db=db, id=id)
    if db_citas is None:
        raise HTTPException(status_code=404, detail="La cita no existe")
    return  db_citas

