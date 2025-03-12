from sqlalchemy.orm import Session
from models.rol_model import Rol
from schemas import rol_schema as schemas


def obtener_todos_los_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Rol).offset(skip).limit(limit).all()

def obtener_rol_por_ID(db: Session, id: int):
    return db.query(Rol).filter(Rol.id == id).first()

def crear_rol(db: Session, rol: schemas.RolCreate):
    db_rol = Rol(**rol.dict())
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def actualizar_rol(db: Session, id: int, rol: schemas.RolUpdate):
    db_rol = db.query(Rol).filter(Rol.id == id).first()
    if db_rol:
        for var, value in vars(rol).items():
            setattr(db_rol, var, value) if value else None
        db.commit()
        db.refresh(db_rol)
    return db_rol

def eliminar_rol(db: Session, id: int):
    db_rol = db.query(Rol).filter(Rol.id == id).first()
    if db_rol:
        db.delete(db_rol)
        db.commit()
    return db_rol

