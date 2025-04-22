from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from config.db import SessionLocal
from crud import persona_crud as crud
from models.persona_model import Personas
from schemas import persona_schema as schemas
from typing import List, Annotated

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




@persona_routes.post("/personas", response_model=schemas.Persona)
def crear_personas(
    personas: schemas.PersonaSimpleCreate, 
    db: Session = Depends(get_db)
):
    db_persona = crud.obtener_persona_por_rfc(db=db, rfc=personas.rfc)
    if db_persona:
        raise HTTPException(status_code=400, detail="La persona ya existe")
    return crud.crear_persona(db=db, persona=personas)


@persona_routes.post("/registro", response_model=dict)
def crear_persona(
    persona_data: Annotated[
        schemas.PersonaCreate,
        Body(
            examples={
                "persona_fisica": {
                    "summary": "Registro de persona física",
                    "description": "Ejemplo de cómo registrar una persona física con todos sus datos.",
                    "value": {
                        "tipo": "Fisica",
                        "datos_generales": {
                            "rfc": "ABC123456XYZ",
                            "estatus": 1
                        },
                        "datos_especificos": {
                            "nombre": "Juan",
                            "apellido_paterno": "Pérez",
                            "apellido_materno": "López",
                            "genero": "Masculino",
                            "curp": "CURP123456HDFLZR01",
                            "titulo_cortesia": "Sr.",
                            "direccion": "Calle Falsa 123",
                            "fecha_nacimiento": "1990-01-01",
                            "estatus": 1
                        }
                    }
                },
                "persona_moral": {
                    "summary": "Registro de persona moral",
                    "description": "Ejemplo de cómo registrar una persona moral con su razón social.",
                    "value": {
                        "tipo": "Moral",
                        "datos_generales": {
                            "rfc": "XYZ654321ABC",
                            "estatus": 1
                        },
                        "datos_especificos": {
                            "razon_social": "Empresa S.A. de C.V.",
                            "direccion": "Av. Empresa 456",
                            "estatus": 1
                        }
                    }
                }
            }
        )
    ],
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

