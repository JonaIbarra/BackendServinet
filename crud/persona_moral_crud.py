from sqlalchemy.orm import Session
from models.persona_moral_model import Personas_Moral
from schemas import persona_moral_schema as schemas

def obtener_todas_las_personas_morales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Personas_Moral).offset(skip).limit(limit).all()

def obtener_personas_morales_por_ID(db: Session, id: int):
    return db.query(Personas_Moral).filter(Personas_Moral.id == id).first()

def crear_personas_morales(db: Session, personas: schemas.PersonaMoralCreate):
    db_persona_moral = Personas_Moral(**personas.dict())
    db.add(db_persona_moral)
    db.commit()
    db.refresh(db_persona_moral)
    return db_persona_moral

def actualizar_personas_morales(db: Session, id: int, personas: schemas.PersonaMoralUpdate):
    db_persona_moral = db.query(Personas_Moral).filter(Personas_Moral.id == id).first()
    if db_persona_moral:
        for var, value in vars(personas).items():
            setattr(db_persona_moral, var, value) if value else None
        db.commit()
        db.refresh(db_persona_moral)
    return db_persona_moral

def eliminar_personas_morales(db: Session, id: int):
    db_persona_moral = db.query(Personas_Moral).filter(Personas_Moral.id == id).first()
    if db_persona_moral:
        db.delete(db_persona_moral)
        db.commit()
    return db_persona_moral