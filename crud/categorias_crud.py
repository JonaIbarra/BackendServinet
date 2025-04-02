from sqlalchemy.orm import Session
from models.categorias_model import Categorias
from schemas import categorias_schema as schemas


def obtener_todas_las_categorias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Categorias).offset(skip).limit(limit).all()

def obtener_categorias_por_ID(db:Session, id: int):
    return db.query(Categorias).filter(Categorias.id == id).first()

def validar_categoria_existente(db: Session, nombre: str):
    return  db.query(Categorias).filter(Categorias.nombre == nombre).first()
    

def crear_categorias(db: Session, categorias):
    db_categorias = Categorias(**categorias.dict())
    db.add(db_categorias)
    db.commit()
    db.refresh(db_categorias)
    return db_categorias    

def actualizar_categorias(db: Session, id: int, categorias: schemas.CategoriasUpdate):
    db_categorias = db.query(Categorias).filter(Categorias.id == id).first()
    if db_categorias:
        for var, value in vars(categorias).items():
            setattr(db_categorias, var, value) if value else None
        db.commit()
        db.refresh(db_categorias)
    return db_categorias


def eliminar_categorias(db: Session, id: int):
    db_categorias = db.query(Categorias).filter(Categorias.id == id).first()
    if db_categorias:
        db.delete(db_categorias)
        db.commit()
    return db_categorias

