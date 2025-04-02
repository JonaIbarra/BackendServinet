from fastapi import HTTPException
from requests import Session
from models.servicios_model import Servicios
from schemas import servicios_schema as schemas


def obtener_todas_los_servicios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Servicios).offset(skip).limit(limit).all()

def obtener_servicios_por_ID(db: Session, id: int):
    return db.query(Servicios).filter(Servicios.id == id).first()

def obtener_servicios_disonibles(db: Session):
    return db.query(Servicios).filter(Servicios.estatus == 1).all()

def obtener_servicios_por_categoria(db: Session, categoria_id: int):
    return db.query(Servicios).filter(Servicios.categoria_id == categoria_id, Servicios.estatus == 1).all()

def obtener_servicios_por_sucursal(db: Session, sucursal_id: int):
    return db.query(Servicios).filter(Servicios.sucursal_id == sucursal_id).all()

def obtener_servicios_por_precios(db: Session):
    return db.query(Servicios).filter(Servicios.estatus == 1).order_by(Servicios.precio.asc()).all()





def validar_servicio_existente(db: Session, nombre: str, sucursal_id: int):
    db_servicio = db.query(Servicios).filter(
        Servicios.nombre == nombre,
        Servicios.sucursal_id == sucursal_id
    ).first()
    if db_servicio:
        raise HTTPException(
            status_code=400, 
            detail="El servicio ya está registrado en esta sucursal"
        )



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