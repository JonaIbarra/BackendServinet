from typing import List
from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from config.db import SessionLocal
from crud import sucursales_crud as crud
from schemas import sucursales_schema as schemas
from services.portador_token import Portador




sucursales_routes = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@sucursales_routes.get("/sucursales", response_model=List[schemas.Sucursales], dependencies=[Depends(Portador())])
def obtener_todos_las_sucursales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_sucursales = crud.obtener_todas_las_sucursales(db=db, skip=skip, limit=limit)
    return db_sucursales


@sucursales_routes.get("/sucursales/{id}", response_model=schemas.Sucursales, dependencies=[Depends(Portador())])
def obtener_sucursales_por_ID(id: int, db: Session = Depends(get_db)):
    sucursales_routes = crud.obtener_sucursales_por_ID(db=db, id=id)
    if sucursales_routes is None:
        raise HTTPException(status_code=404, detail="La sucursal no existe")
    return sucursales_routes



@sucursales_routes.post("/registro_sucursal", response_model=schemas.Sucursales, dependencies=[Depends(Portador())])
def crear_sucursal(sucursales: schemas.SucursalesCreate, db: Session = Depends(get_db)):
    db_sucursales = crud.obtener_sucursal_por_nombre_y_ubicacion(db=db, nombre=sucursales.datos_sucursal.nombre)
    if db_sucursales:
        raise HTTPException(status_code=400, detail="La sucursal ya existe")
    return crud.crear_sucursal_completa(db=db, sucursal=sucursales)



@sucursales_routes.put("/sucursales/{id}", response_model=schemas.Sucursales, dependencies=[Depends(Portador())])
def actualizar_sucursales(id: int, sucursales: schemas.SucursalesUpdate, db: Session = Depends(get_db)):
    db_sucursales = crud.actualizar_sucursales(db=db, id=id, sucursales=sucursales)
    if db_sucursales is None:
        raise HTTPException(status_code=404, detail="La sucursal no existe")
    return db_sucursales


@sucursales_routes.delete("/sucursales/{id}", response_model=schemas.Sucursales, dependencies=[Depends(Portador())])
def eliminar_sucursales(id: int, db: Session = Depends(get_db)):
    db_sucursales = crud.eliminar_sucursales(db=db, id=id)
    if db_sucursales is None:
        raise HTTPException(status_code=404, detail="La sucrsale no existe")
    return  db_sucursales

