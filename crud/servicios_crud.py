from requests import Session
from models.servicios_model import Servicios
from schemas import servicios_schema as schemas


def obtener_todas_los_servicios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Servicios).offset(skip).limit(limit).all()

def obtener_servicios_por_ID(db: Session, id: int):
    return db.query(Servicios).filter(Servicios.id == id).first()

def crear_servicios(db: Session, servicios: schemas.ServiciosCreate):
    db_servicios = Servicios(**servicios.dict())
    db.add(db_servicios)
    db.commit()
    db.refresh(db_servicios)
    return db_servicios

def actualizar_servicios(db: Session, id: int, servicios: schemas.ServiciosUpdate):
    db_servicios = db.query(Servicios).filter(Servicios.id == id).first()
    if db_servicios:
        for var, value in vars(servicios).items():
            setattr(db_servicios, var, value) if value else None
        db.commit()
        db.refresh(db_servicios)
    return db_servicios

def eliminar_servicios(db: Session, id: int):
    db_servicios = db.query(Servicios).filter(Servicios.id == id).first()
    if db_servicios:
        db.delete(db_servicios)
        db.commit()
    return db_servicios