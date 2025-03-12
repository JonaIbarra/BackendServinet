from sqlalchemy.orm import Session
from models.medio_contactos_model import Medio_Contactos


def obtener_todos_medios_contactos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Medio_Contactos).offset(skip).limit(limit).all()
