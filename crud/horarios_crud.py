from sqlalchemy.orm import Session
from models.horarios_model import Horarios
from schemas import horarios_schema as schemas


def obtener_todos_los_horarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Horarios).offset(skip).limit(limit).all()


def obtener_horarios_por_ID(db: Session, id: int):
    return db.query(Horarios).filter(Horarios.id == id).first()

# def crear_horarios(db: Session, horarios: schemas.HorariosCreate):
#     db_horarios = Servicios(**servicios.dict())
#     db.add(db_horarios)
#     db.commit()
#     db.refresh(db_horarios)
#     return db_horarios1

# def actualizar_servicios(db: Session, id: int, servicios: schemas.ServiciosUpdate):
#     db_servicios = db.query(Servicios).filter(Servicios.id == id).first()
#     if db_servicios:
#         for var, value in vars(servicios).items():
#             setattr(db_servicios, var, value) if value else None
#         db.commit()
#         db.refresh(db_servicios)
#     return db_servicios

# def eliminar_servicios(db: Session, id: int):
#     db_servicios = db.query(Servicios).filter(Servicios.id == id).first()
#     if db_servicios:
#         db.delete(db_servicios)
#         db.commit()
#     return db_servicios


