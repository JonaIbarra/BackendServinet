from sqlalchemy.orm import Session
from models.cancelaciones_model import Cancelaciones



def obtener_todas_las_cancelaciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cancelaciones).offset(skip).limit(limit).all()