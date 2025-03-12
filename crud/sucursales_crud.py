from requests import Session
from models.sucursales_model import Sucursales
from schemas import sucursales_schema as schemas


def obtener_todas_las_sucursales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Sucursales).offset(skip).limit(limit).all()

def obtener_sucursales_por_ID(db: Session, id: int):
    return db.query(Sucursales).filter(Sucursales.id == id).first()

def crear_sucursales(db: Session, sucursales: schemas.SucursalesCreate):
    db_sucursales = Sucursales(**sucursales.dict())
    db.add(db_sucursales)
    db.commit()
    db.refresh(db_sucursales)
    return db_sucursales

def actualizar_sucursales(db: Session, id: int, sucursales: schemas.SucursalesUpdate):
    db_sucursales = db.query(Sucursales).filter(Sucursales.id == id).first()
    if db_sucursales:
        for var, value in vars(sucursales).items():
            setattr(db_sucursales, var, value) if value else None
        db.commit()
        db.refresh(db_sucursales)
    return db_sucursales

def eliminar_sucursales(db: Session, id: int):
    db_sucursales = db.query(Sucursales).filter(Sucursales.id == id).first()
    if db_sucursales:
        db.delete(db_sucursales)
        db.commit()
    return db_sucursales
