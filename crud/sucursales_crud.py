from sqlite3 import IntegrityError
from fastapi import HTTPException
from requests import Session
from models.horarios_model import Horarios
from models.sucursales_model import Sucursales
from models.ubicaciones_model import Ubicaciones
from schemas import sucursales_schema as schemas



def obtener_todas_las_sucursales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Sucursales).offset(skip).limit(limit).all()

def obtener_sucursales_por_ID(db: Session, id: int):
    return db.query(Sucursales).filter(Sucursales.id == id).first()

def obtener_sucursal_por_nombre_y_ubicacion(db: Session, nombre: str):
    return db.query(Sucursales).filter(Sucursales.nombre == nombre).first()



def crear_sucursal_completa(sucursal: schemas.SucursalesCreate, db: Session):
    try:
        # 1. Crear la sucursal
        db_sucursales = Sucursales(**sucursal.datos_sucursal.dict())
        db.add(db_sucursales)
        db.flush()  # Genera el ID de la sucursal

        # 2. Crear la ubicación
        db_ubicaciones = Ubicaciones(
            sucursal_id=db_sucursales.id,
            **sucursal.datos_ubicacion.dict()
        )
        db.add(db_ubicaciones)

        # 3. Crear los 7 horarios (uno por día)
        dias = [
            sucursal.lunes,
            sucursal.martes,
            sucursal.miercoles,
            sucursal.jueves,
            sucursal.viernes,
            sucursal.sabado,
            sucursal.domingo
        ]

        for horario_dia in dias:
            db_horario = Horarios(
                sucursal_id=db_sucursales.id,
                **horario_dia.dict()
            )
            db.add(db_horario)

        # 4. Confirmar todo en la base de datos
        db.commit()
        db.refresh(db_sucursales)
        return db_sucursales

    


    except IntegrityError as e:
        db.rollback()  # Revierte en caso de error
        raise HTTPException(status_code=400, detail="Error de integridad")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))



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
