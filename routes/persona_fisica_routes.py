from fastapi import APIRouter, HTTPException, Depends
from requests import Session
from config.db import SessionLocal
from crud import persona_fisica_crud as crud
from schemas import persona_fisica_schema as schemas
from typing import List

persona_fisica_routes = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@persona_fisica_routes.get("/personas_fisicas", response_model=List[schemas.PersonaFisica])
def obtener_todas_las_personas_fisicas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_persona_fisica = crud.obtener_todas_las_personas_fisicas(db=db, skip=skip, limit=limit)
    return db_persona_fisica



@persona_fisica_routes.get("/personas_fisicas/{id}", response_model=schemas.PersonaFisica)
def obtener_personas_fisicas_por_ID(id: int, db: Session = Depends(get_db)):
    db_personas_fisica = crud.obtener_personas_fisicas_por_ID(db=db, id=id)
    if db_personas_fisica is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return db_personas_fisica


@persona_fisica_routes.post("/personas_fisicas", response_model=schemas.PersonaFisica)
def crear_personas_fisicas(personas: schemas.PersonaFisicaCreate, db: Session = Depends(get_db)):
    db_personas_fisica = crud.obtener_personas_fisicas_por_ID(db=db, id=personas.id)
    if db_personas_fisica:
        raise HTTPException(status_code=400, detail="La persona ya existe")
    return crud.crear_personas_fisicas(db=db, personas=personas)


# @persona_fisica_routes.get("/registro/fisica/")
# def registrar_persona_fisica(personas: schemas.PersonaFisicaCreate, db: Session = Depends(get_db)):
#     # Iniciar transacción
#     persona = persona_model.Personas(tipo="Fisica", estado="Activo")
#     db.add(persona)
#     db.commit()
#     db.refresh(persona)

#     persona_fisica = PersonaFisica(
#         persona_id=persona.id,
#         nombre=persona_data.nombre,
#         apellido_paterno=persona_data.apellido_paterno,
#         apellido_materno=persona_data.apellido_materno,
#         genero=persona_data.genero,
#         curp=persona_data.curp,
#         rfc=persona_data.rfc,
#         direccion=persona_data.direccion,
#         fecha_nacimiento=persona_data.fecha_nacimiento
#     )
#     db.add(persona_fisica)
#     db.commit()
#     db.refresh(persona_fisica)

#     return {"message": "Registro exitoso", "persona_id": persona.id}







@persona_fisica_routes.put("/personas_fisicas/{id}", response_model=schemas.PersonaFisica)
def actualizar_personas_fisicas(id: int, personas: schemas.PersonaFisicaUpdate, db: Session = Depends(get_db)):
    db_personas_fisica = crud.actualizar_personas_fisicas(db=db, id=id, personas=personas)
    if db_personas_fisica is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return db_personas_fisica

@persona_fisica_routes.delete("/personas_fisicas/{id}", response_model=schemas.PersonaFisica)
def eliminar_personas_fisicas(id: int, db: Session = Depends(get_db)):
    db_personas_fisica = crud.eliminar_personas_fisicas(db=db, id=id)
    if db_personas_fisica is None:
        raise HTTPException(status_code=404, detail="La persona no existe")
    return  db_personas_fisica

