from datetime import datetime
from sqlalchemy.orm import Session
from models.promociones_model import Promociones
from schemas import promociones_schema as schemas

def obtener_todas_las_promociones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Promociones).offset(skip).limit(limit).all()

def obtener_promociones_por_ID(db: Session, id: int):   
    return db.query(Promociones).filter(Promociones.id == id).first()


def existe_promocion(db: Session, servico_id: int, titulo: str) -> bool:
    now = datetime.now()
    promo = db.query(Promociones).filter(
        Promociones.servicio_ID == servico_id,
        Promociones.titulo == titulo,
        Promociones.estatus == 1,
        Promociones.hora_inicio <= now,
        Promociones.hora_fin >= now
    ).first()
    return promo
    
def crear_promociones(db: Session, promociones: schemas.PromocionesCreate):
    db_promociones = Promociones(**promociones.model_dump())
    db.add(db_promociones)
    db.commit()
    db.refresh(db_promociones)
    return db_promociones

def actualizar_promociones(db: Session, id: int, promociones: schemas.PromocionesUpdate):
    db_promociones = db.query(Promociones).filter(Promociones.id == id).first()
    if db_promociones:
        for var, value in vars(promociones).items():
            setattr(db_promociones, var, value) if value else None
        db.commit()
        db.refresh(db_promociones)
    return db_promociones

def eliminar_promociones(db: Session, id: int):
    db_promociones = db.query(Promociones).filter(Promociones.id == id).first()
    if db_promociones:
        db.delete(db_promociones)
        db.commit()
    return db_promociones

