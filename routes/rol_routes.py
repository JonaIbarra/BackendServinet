from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import SessionLocal
from crud import rol_crud as crud
from schemas import rol_schema as schemas


rol_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rol_routes.get("/roles", response_model=List[schemas.Rol])
def obtener_todos_los_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_rol = crud.obtener_todos_los_roles(db=db, skip=skip, limit=limit)
    return db_rol

@rol_routes.get("/roles/{nombre}", response_model=schemas.Rol)
def obtener_rol_por_nombre(nombreRol: str, db: Session = Depends(get_db)):
    db_rol = crud.obtener_rol_por_nombre(db=db, nombre_rol = nombreRol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="El rol no existe")
    return db_rol  

@rol_routes.post("/roles", response_model=schemas.Rol)
def crear_rol(rol: schemas.RolCreate, db: Session = Depends(get_db)):
    db_rol = crud.obtener_rol_por_nombre(db=db, nombre_rol = rol.nombre_rol)
    if db_rol:
        raise HTTPException(status_code=400, detail="El rol ya existe")
    return crud.crear_rol(db=db, rol=rol)


@rol_routes.put("/roles/{id}", response_model=schemas.Rol) 
def actualizar_rol(id: int, rol: schemas.RolUpdate, db: Session = Depends(get_db)):
    db_rol = crud.actualizar_rol(db=db, id=id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="El rol no existe")
    return db_rol

@rol_routes.delete("/roles/{id}", response_model=schemas.Rol)
def eliminar_rol(id: int, db: Session = Depends(get_db)):
    db_rol = crud.eliminar_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="El rol no existe")
    return  db_rol
