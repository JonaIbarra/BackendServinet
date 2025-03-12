from sqlalchemy.orm import Session  
from models.usuario_rol_model import UsuarioRol




def obtener_todos_los_usuarios_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UsuarioRol).offset(skip).limit(limit).all()

def obtener_usuario_rol_por_rol_ID(db: Session, id: int):
    return db.query(UsuarioRol).filter(UsuarioRol.rol_ID == id).first()

def obtener_usuario_rol_por_usuario_ID(db: Session, id: int):    
    return db.query(UsuarioRol).filter(UsuarioRol.usuario_ID == id).first()



