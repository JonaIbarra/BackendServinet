from sqlalchemy.orm import Session
from models.persona_fisica_model import Personas_Fisicas
from schemas import persona_fisica_schema as schemas

def obtener_todas_las_personas_fisicas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Personas_Fisicas).offset(skip).limit(limit).all()

def obtener_personas_fisicas_por_ID(db: Session, id: int):
    return db.query(Personas_Fisicas).filter(Personas_Fisicas.id == id).first()

def crear_personas_fisicas(db: Session, personas: schemas.PersonaFisicaCreate):
    db_persona_fisica = Personas_Fisicas(**personas.dict())
    db.add(db_persona_fisica)
    db.commit()
    db.refresh(db_persona_fisica)
    return db_persona_fisica

def actualizar_personas_fisicas(db: Session, id: int, personas: schemas.PersonaFisicaUpdate):
    db_persona_fisica = db.query(Personas_Fisicas).filter(Personas_Fisicas.id == id).first()
    if db_persona_fisica:
        for var, value in vars(personas).items():
            setattr(db_persona_fisica, var, value) if value else None
        db.commit()
        db.refresh(db_persona_fisica)
    return db_persona_fisica

def eliminar_personas_fisicas(db: Session, id: int):
    db_persona_fisica = db.query(Personas_Fisicas).filter(Personas_Fisicas.id == id).first()
    if db_persona_fisica:
        db.delete(db_persona_fisica)
        db.commit()
    return db_persona_fisica