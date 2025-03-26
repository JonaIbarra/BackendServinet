from typing import List
from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from crud import categorias_crud as crud
from schemas import categorias_schema as schemas
from config.db import SessionLocal

categorias_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@categorias_routes.get("/categorias", response_model=List[schemas.Categorias])
def obtener_todas_las_categorias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_categorias = crud.obtener_todas_las_categorias(db=db, skip=skip, limit=limit)
    return db_categorias

@categorias_routes.get("/categorias/{nombre}", response_model=schemas.Categorias)
def validar_categoria_existente(nombre: str, db: Session = Depends(get_db)):
    db_categorias = crud.validar_categoria_existente(db=db, nombre =nombre)
    if db_categorias is None:
        raise HTTPException(status_code=404, detail="La Categoria no existe")
    return db_categorias

@categorias_routes.post("/categorias", response_model=schemas.Categorias)
def crear_categorias(categorias: schemas.CategoriasCreate, db: Session = Depends(get_db)):
    db_categorias = crud.validar_categoria_existente(db=db, nombre=categorias.nombre)
    if db_categorias:
        raise HTTPException(status_code=400, detail="La categoria ya existe")
    return crud.crear_categorias(db=db, categorias =categorias)

@categorias_routes.put("/categorias/{id}", response_model=schemas.Categorias)
def actualizar_categorias(id: int, categorias: schemas.CategoriasUpdate, db: Session = Depends(get_db)):
    db_categorias = crud.actualizar_categorias(db=db, id=id, categorias=categorias)
    if db_categorias is None:
        raise HTTPException(status_code=404, detail="La categoria no existe")
    return db_categorias

@categorias_routes.delete("/catgorias/{id}", response_model=schemas.Categorias)
def eliminar_categorias(id: int, db: Session = Depends(get_db)):
    db_categorias = crud.eliminar_categorias(db=db, id=id)
    if db_categorias is None:
        raise HTTPException(status_code=404, detail="La Categoria no existe")
    return  db_categorias


