from sqlalchemy.orm import Session
from models.horarios_model import Horarios
from schemas import horarios_schema as schemas


def obtener_todos_los_horarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Horarios).offset(skip).limit(limit).all()


def obtener_horarios_por_ID(db: Session, id: int):
    return db.query(Horarios).filter(Horarios.id == id).first()

