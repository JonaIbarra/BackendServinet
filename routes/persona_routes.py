from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.db import SessionLocal
from crud import persona_crud as crud
from models.persona_model import Personas
from schemas import persona_schema as schemas
from typing import List

persona_routes = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@persona_routes.get("/personas", response_model=List[schemas.Persona])
def obtener_todas_las_persona(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_persona = crud.obtener_todas_las_personas(db=db, skip=skip, limit=limit)
    return db_persona

@persona_routes.get("/personas/{id}", response_model=schemas.Persona)
def obtener_persona_por_ID(id: int, db: Session = Depends(get_db)):
    db_persona = crud.obtener_persona_por_ID(db=db, id=id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return db_persona


# @persona_routes.post("/personas", response_model=schemas.Persona)  # Response SI incluye id
# def crear_persona(
#     persona: schemas.PersonaCreate,  
#     db: Session = Depends(get_db)
# ):

#     db_persona = crud.obtener_persona_por_CURP(db, persona.CURP)
#     if db_persona:
#         raise HTTPException(status_code=400, detail="La CURP ya está registrada")
    
#     return crud.crear_persona(db=db, persona=persona)

# @persona_routes.post("/personas", response_model=schemas.Persona)
# def crear_personas(personas: schemas.PersonaCreate, db: Session = Depends(get_db)):
#     db_persona = crud.obtener_persona_por_rfc(db=db, rfc=personas.rfc)
#     if db_persona:
#         raise HTTPException(status_code=400, detail="La persona ya existe")
#     return crud.crear_persona(db=db, persona = personas)  

@persona_routes.post("/personas", response_model=schemas.Persona)
def crear_personas(
    personas: schemas.PersonaCreate, 
    db: Session = Depends(get_db)
):
    db_persona = crud.obtener_persona_por_rfc(db=db, rfc=personas.datos_generales.rfc)
    if db_persona:
        raise HTTPException(status_code=400, detail="La persona ya existe")
    
    persona_creada = crud.crear_persona(db=db, persona=personas)
    return persona_creada  #


@persona_routes.post("/registro", response_model=dict)
def crear_persona(
    persona_data: schemas.PersonaCreate,
    db: Session = Depends(get_db)
):
    # Validar RFC único
    if db.query(Personas).filter(Personas.rfc == persona_data.datos_generales.rfc).first():
        raise HTTPException(status_code=400, detail="RFC ya registrado")

    # Crear persona y subtabla
    persona_creada = crud.crear_persona_completa(db, persona_data)
    return {
        "id": persona_creada.id,
        "tipo": persona_creada.tipo.value,
        "rfc": persona_creada.rfc,
        "estatus": persona_creada.estatus
    }



@persona_routes.put("/personas/{id}", response_model=schemas.Persona)
def actualizar_persona(id: int, personas: schemas.PersonaUpdate, db: Session = Depends(get_db)):
    db_persona = crud.actualizar_persona(db=db, id=id, personas=personas)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return db_persona

@persona_routes.delete("/personas/{id}", response_model=schemas.Persona)
def eliminar_persona(id: int, db: Session = Depends(get_db)):
    db_persona = crud.eliminar_persona(db=db, id=id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return  db_persona

