from sqlalchemy.orm import Session  
from models.usuario_rol_model import UsuarioRol


def obtener_todos_los_usuarios_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UsuarioRol).offset(skip).limit(limit).all()


def obtener_usuario_rol_por_rol_ID(db: Session, id: int):
    return db.query(UsuarioRol).filter(UsuarioRol.rol_ID == id).first()


def obtener_usuario_rol_por_usuario_ID(db: Session, id: int):    
    return db.query(UsuarioRol).filter(UsuarioRol.usuario_ID == id).first()


def crear_usuario_rol(db: Session, usuario_rol: UsuarioRol):
    try:
        db_usuario_rol = UsuarioRol(**usuario_rol.model_dump())
        db.add(db_usuario_rol)
        db.commit()
        db.refresh(db_usuario_rol)
        return db_usuario_rol
    except Exception as e:
        db.rollback()
        raise Exception(f"Error al crear usuario_rol: {e}")


def actualizar_usuario_rol(db: Session, id: int, usuario_rol: UsuarioRol):
    db_usuario_rol = db.query(UsuarioRol).filter(UsuarioRol.id == id).first()
    if not db_usuario_rol:
        return None

    # Actualizar solo los campos que no sean None
    data_update = {key: value for key, value in usuario_rol.model_dump().items() if value is not None}
    
    try:
        db.query(UsuarioRol).filter(UsuarioRol.id == id).update(data_update)
        db.commit()
        db.refresh(db_usuario_rol)
        return db_usuario_rol
    except Exception as e:
        db.rollback()
        raise Exception(f"Error al actualizar usuario_rol: {e}")


def eliminar_usuario_rol(db: Session, id: int):
    db_usuario_rol = db.query(UsuarioRol).filter(UsuarioRol.id == id).first()
    if not db_usuario_rol:
        return None
    
    try:
        db.delete(db_usuario_rol)
        db.commit()
        return db_usuario_rol
    except Exception as e:
        db.rollback()
        raise Exception(f"Error al eliminar usuario_rol: {e}")
    
    