from fastapi import APIRouter, Depends, HTTPException
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

@ubicaciones_router.get("/ubicaciones/{id}", response_model=schemas.Ubicaciones)
def obtener_ubicacion_por_ID(id: int, db: Session = Depends(get_db)):
    db_ubicaciones = crud.obtener_ubicacion_por_ID(db=db, id=id)
    if db_ubicaciones is None:
        raise HTTPException(status_code=404, detail="La ubicacion no existe")
    return db_ubicaciones

@ubicaciones_router.post("/ubicaciones", response_model=schemas.Ubicaciones)
def crear_ubicacion(ubicacion_create: schemas.UbicacionesCreate, db: Session = Depends(get_db)):
    # Validación por los campos de la ubicación
    db_ubicaciones = crud.obtener_ubicacion_por_direccion(
        db=db,
        pais=ubicacion_create.pais,
        estado=ubicacion_create.estado,
        ciudad=ubicacion_create.ciudad,
        colonia=ubicacion_create.colonia,
        calle=ubicacion_create.calle,
        numero_exterior=ubicacion_create.numero_exterior,
        codigo_postal=ubicacion_create.codigo_postal
    )
    if db_ubicaciones:
        raise HTTPException(status_code=400, detail="La ubicación ya existe")

    return crud.crear_ubicacion(db=db, ubicaciones=ubicacion_create)


@ubicaciones_router.put("/ubicaciones/{id}", response_model=schemas.Ubicaciones)
def actualizar_ubicacion(id: int, ubicacion: schemas.UbicacionesUpdate, db: Session = Depends(get_db)):
    db_ubicaciones = crud.actualizar_ubicaciones(db=db, id=id, ubicaciones = ubicacion)
    if db_ubicaciones is None:
        raise HTTPException(status_code=404, detail="La ubicacion no existe")
    return db_ubicaciones

@ubicaciones_router.delete("/ubicaciones/{id}", response_model=schemas.Ubicaciones)
def eliminar_ubicacion(id: int, db: Session = Depends(get_db)):
    db_citas = crud.eliminar_ubicaciones(db=db, id=id)
    if db_citas is None:
        raise HTTPException(status_code=404, detail="La ubicacion no existe")
    return  db_citas

