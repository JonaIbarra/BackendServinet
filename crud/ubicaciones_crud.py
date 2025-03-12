from requests import Session
from models.ubicaciones_model import Ubicaciones


def obtener_todas_las_ubicaciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ubicaciones).offset(skip).limit(limit).all()

