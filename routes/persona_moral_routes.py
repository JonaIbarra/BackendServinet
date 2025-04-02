from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.db import SessionLocal
from crud import persona_moral_crud as crud
from schemas import persona_moral_schema as schemas
from typing import List

persona_moral_routes = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@persona_moral_routes.get("/personas_morales", response_model=List[schemas.PersonaMoral])
def obtener_todas_las_personas_morales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_persona_moral = crud.obtener_todas_las_personas_morales(db=db, skip=skip, limit=limit)
    return db_persona_moral

@persona_moral_routes.get("/personas_morales/{id}", response_model=schemas.PersonaMoral)
def obtener_personas_morales_por_ID(id: int, db: Session = Depends(get_db)):
    db_persona_moral = crud.obtener_personas_morales_por_ID(db=db, id=id)
    if db_persona_moral is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return db_persona_moral


@persona_moral_routes.post("/personas_morales", response_model=schemas.PersonaMoral)
def crear_personas_morales(personas: schemas.PersonaMoralCreate, db: Session = Depends(get_db)):
    db_persona_moral = crud.obtener_personas_morales_por_ID(db=db, id=personas.id)
    if db_persona_moral:
        raise HTTPException(status_code=400, detail="La persona ya existe")
    return crud.crear_personas_morales(db=db, personas=personas)

@persona_moral_routes.put("/personas_morales/{id}", response_model=schemas.PersonaMoral)
def actualizar_personas_morales(id: int, personas: schemas.PersonaMoralUpdate, db: Session = Depends(get_db)):
    db_persona_moral = crud.actualizar_personas_morales(db=db, id=id, personas=personas)
    if db_persona_moral is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return db_persona_moral

@persona_moral_routes.delete("/personas_morales/{id}", response_model=schemas.PersonaMoral)
def eliminar_personas_morales(id: int, db: Session = Depends(get_db)):
    db_persona_moral = crud.eliminar_personas_morales(db=db, id=id)
    if db_persona_moral is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return  db_persona_moral

