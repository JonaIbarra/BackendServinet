from doctest import debug
from sqlite3 import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.persona_fisica_model import Personas_Fisicas
from models.persona_model import Personas, TipoPersonaEnum
from models.persona_moral_model import Personas_Moral
from schemas import persona_schema as schemas

def obtener_todas_las_personas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Personas).offset(skip).limit(limit).all()

def obtener_persona_por_rfc(db: Session, rfc: str):
    return db.query(Personas).filter(Personas.rfc == rfc).first()

# def obtener_personas_por_ID(db: Session, id: int):
#     return db.query(Personas).filter(Personas.id == id).first()

# def crear_persona(db: Session, persona: schemas.PersonaCreate):
#     db_persona = Personas(**persona.model_dump())
#     db.add(db_persona)
#     db.commit()
#     db.refresh(db_persona)
#     return db_persona


def crear_persona(db: Session, persona: schemas.PersonaCreate):
    persona_data = persona.model_dump()
    db_persona = Personas(**persona_data)
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona

def crear_persona_completa(db: Session, persona_data: schemas.PersonaCreate):
    try:
        # Crear registro en Personas (no se necesita db.begin())
        db_persona = Personas(
            tipo=persona_data.tipo,
            rfc=persona_data.datos_generales.rfc,
            estatus=persona_data.datos_generales.estatus
        )
        db.add(db_persona)
        db.flush()  # Obtiene el ID sin commit

        # Crear subtabla según el tipo
        if persona_data.tipo == schemas.TipoPersonaEnum.Fisica:
            subtabla = Personas_Fisicas(
                persona_ID=db_persona.id,
                **persona_data.datos_especificos.model_dump()
            )
        else:
            subtabla = Personas_Moral(
                persona_ID=db_persona.id,
                **persona_data.datos_especificos.model_dump()
            )

        db.add(subtabla)
        db.commit()  # Confirma ambos registros en una transacción
        db.refresh(db_persona)
        return db_persona

    except IntegrityError as e:
        db.rollback()  # Revierte en caso de error
        raise HTTPException(status_code=400, detail="Error de integridad")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def actualizar_persona(db: Session, id: int, personas: schemas.PersonaUpdate):
    db_persona = db.query(Personas).filter(Personas.id == id).first()
    if db_persona:
        for var, value in vars(personas).items():
            setattr(db_persona, var, value) if value else None
        db.commit()
        db.refresh(db_persona)
    return db_persona

def eliminar_persona(db: Session, id: int):
    db_persona = db.query(Personas).filter(Personas.id == id).first()
    if db_persona:
        db.delete(db_persona)
        db.commit()
    return db_persona