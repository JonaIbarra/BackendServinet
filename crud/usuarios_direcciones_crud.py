from sqlalchemy.orm import Session  
from models.usuarios_direcciones_model import UsuarioDirecciones




def obtener_todos_los_usuarios_direcciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UsuarioDirecciones).offset(skip).limit(limit).all()

def obtener_usuarios_direcciones_por_ID(db: Session, id: int):
    return db.query(UsuarioDirecciones).filter(UsuarioDirecciones.id == id).first()

def crear_usuarios_direcciones(db: Session, usuarios_direcciones):
    db_usuarios_direcciones = UsuarioDirecciones(**usuarios_direcciones.dict())
    db.add(db_usuarios_direcciones)
    db.commit()
    db.refresh(db_usuarios_direcciones)
    return db_usuarios_direcciones

def actualizar_usuarios_direcciones(db: Session, id: int, usuarios_direcciones):
    db_usuarios_direcciones = db.query(UsuarioDirecciones).filter(UsuarioDirecciones.id == id).first()      
    if db_usuarios_direcciones:
        for var, value in vars(usuarios_direcciones).items():
            setattr(db_usuarios_direcciones, var, value) if value else None
        db.commit()
        db.refresh(db_usuarios_direcciones)
    return db_usuarios_direcciones

def eliminar_usuarios_direcciones(db: Session, id: int):
    db_usuarios_direcciones = db.query(UsuarioDirecciones).filter(UsuarioDirecciones.id == id).first()
    if db_usuarios_direcciones:
        db.delete(db_usuarios_direcciones)
        db.commit()
    return db_usuarios_direcciones

