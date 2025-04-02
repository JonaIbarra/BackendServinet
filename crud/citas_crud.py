from datetime import date
from sqlalchemy.orm import Session
from models.citas_model import Citas
from schemas import citas_schema as schemas


def obtener_todas_las_citas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Citas).offset(skip).limit(limit).all()


def verificar_cita_por_dia(db: Session, usuario_id: int, fecha: date):
    return db.query(Citas).filter(
        Citas.usuario_ID == usuario_id,
        Citas.estatus == 1,  # Solo citas activas
        Citas.fecha_inicio == fecha  # Mismo día
    ).first()


def crear_cita(db: Session, citas: schemas.CitasCreate):
    db_citas = Citas(**citas.model_dump()) 
    db.add(db_citas)
    db.commit()
    db.refresh(db_citas)
    return db_citas

def actualizar_citas(db: Session, id: int, citas: schemas.CitasUpdate):
    db_citas = db.query(Citas).filter(Citas.id == id).first()
    if db_citas:
        for var, value in vars(citas).items():
            setattr(db_citas, var, value) if value else None
        db.commit()
        db.refresh(db_citas)
    return db_citas

def eliminar_citas(db: Session, id: int):
    db_citas = db.query(Citas).filter(Citas.id == id).first()
    if db_citas:
        db.delete(db_citas)
        db.commit()
    return db_citas