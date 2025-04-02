from sqlalchemy.orm import Session
from models.cancelaciones_model import Cancelaciones



def obtener_todas_las_cancelaciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cancelaciones).offset(skip).limit(limit).all()

def obtener_cancelaciones_por_ID(db: Session, id: int):
    return db.query(Cancelaciones).filter(Cancelaciones.id == id).first()

def obtener_cancelaciones_por_usuario(db: Session, usuario_solicitante: int):
    return db.query(Cancelaciones).filter(Cancelaciones.usuario_solicitante == usuario_solicitante).all()

def obtener_cancelaciones_por_cita(db: Session, cita_ID: int):
    return db.query(Cancelaciones).filter(Cancelaciones.cita_ID == cita_ID).all()


def validar_cancelacion_existente(db: Session, servicio_id: int, usuario_solicitante: int, cita_id: int):
    return db.query(Cancelaciones).filter(
        Cancelaciones.servicio_ID == servicio_id,
        Cancelaciones.usuario_solicitante == usuario_solicitante,
        Cancelaciones.cita_ID == cita_id
    ).first() 

    

def crear_cancelaciones(db: Session, cancelaciones):
    db_cancelaciones = Cancelaciones(**cancelaciones.model_dump())
    db.add(db_cancelaciones)
    db.commit()
    db.refresh(db_cancelaciones)
    return db_cancelaciones

def actualizar_cancelaciones(db: Session, id: int, cancelaciones):
    db_cancelaciones = db.query(Cancelaciones).filter(Cancelaciones.id == id).first()
    if db_cancelaciones:
        for var, value in vars(cancelaciones).items():
            setattr(db_cancelaciones, var, value) if value else None
        db.commit()
        db.refresh(db_cancelaciones)
    return db_cancelaciones

def eliminar_cancelaciones(db: Session, id: int):
    db_cancelaciones = db.query(Cancelaciones).filter(Cancelaciones.id == id).first()
    if db_cancelaciones:
        db.delete(db_cancelaciones)
        db.commit()
    return db_cancelaciones

