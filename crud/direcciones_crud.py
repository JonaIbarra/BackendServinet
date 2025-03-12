from sqlalchemy.orm import Session
from models.direcciones_model import Direcciones
from schemas import direcciones_schema as schemas


def obtener_todas_las_direcciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Direcciones).offset(skip).limit(limit).all()


def obtener_direcciones_por_ID(db: Session, id: int):
    return db.query(Direcciones).filter(Direcciones.id == id).first()

def crear_direcciones(db: Session, direcciones: schemas.DireccionesCreate):
    db_direcciones = Direcciones(**direcciones.dict())
    db.add(db_direcciones)
    db.commit()
    db.refresh(db_direcciones)
    return db_direcciones

def actualizar_direcciones(db: Session, id: int, direcciones: schemas.DireccionesUpdate):    
    db_direcciones = db.query(Direcciones).filter(Direcciones.id == id).first()
    if db_direcciones:
        for var, value in vars(direcciones).items():
            setattr(db_direcciones, var, value) if value else None
        db.commit()
        db.refresh(db_direcciones)
    return db_direcciones

def eliminar_direcciones(db: Session, id: int):
    db_direcciones = db.query(Direcciones).filter(Direcciones.id == id).first()
    if db_direcciones:
        db.delete(db_direcciones)
        db.commit()
    return db_direcciones