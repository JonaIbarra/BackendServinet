from sqlalchemy.orm import Session
from models.canjes_model import Canjes
from schemas import canjes_schema as schemas


def obtener_todos_los_canjes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Canjes).offset(skip).limit(limit).all()

def obtener_canjes_por_ID(db: Session, id: int):
    return db.query(Canjes).filter(Canjes.id == id).first()

def obtener_canjes_por_cita(db: Session, cita_ID: int):
    return db.query(Canjes).filter(Canjes.cita_ID == cita_ID).all()

def obtener_canjes_por_usuario(db: Session, usuario_ID: int):
    return db.query(Canjes).filter(Canjes.usuario_ID == usuario_ID).all()

def validar_canje_existente(db: Session, nombre: str, usuario_ID: int, cita_ID: int):
    return db.query(Canjes).filter(
        Canjes.nombre == nombre,
        Canjes.usuario_ID == usuario_ID,
        Canjes.cita_ID == cita_ID
    ).first()


def crear_canjes(db: Session, canjes: schemas.CanjesCreate):
    db_canjes = Canjes(**canjes.dict())
    db.add(db_canjes)
    db.commit()
    db.refresh(db_canjes)
    return db_canjes

def actualizar_canjes(db: Session, id: int, canjes: schemas.CanjesUpdate):
    db_canjes = db.query(Canjes).filter(Canjes.id == id).first()
    if db_canjes:
        for var, value in vars(canjes).items():
            setattr(db_canjes, var, value) if value else None
        db.commit()
        db.refresh(db_canjes)
    return db_canjes

def eliminar_canjes(db: Session, id: int):
    db_canjes = db.query(Canjes).filter(Canjes.id == id).first()
    if db_canjes:
        db.delete(db_canjes)
        db.commit()
    return db_canjes

