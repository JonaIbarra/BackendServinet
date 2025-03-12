from sqlalchemy.orm import Session
from models.promociones_model import Promociones
from schemas import promociones_schema as schemas

def obtener_todas_las_promociones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Promociones).offset(skip).limit(limit).all()
