from sqlite3 import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.usuario_model import Usuario
from models.usuario_rol_model import UsuarioRol
from crud.rol_crud import crear_rol_predeterminado, obtener_rol_por_nombre
from schemas import usuario_schema as schemas
from services.auth import hash_password


def obtener_todos_los_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()

def obtener_usuario_por_nombre(db: Session, nombre_usuario: str):
    return db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first()

def get_user_by_creentials(db: Session, username: str, password: str):
    return db.query(Usuario).filter((Usuario.nombre_usuario == username),
                                    Usuario.contrasenia == password).first()


def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_password = hash_password(usuario.contrasenia)  # Encripta la contraseña
    db_usuario = Usuario(
        persona_ID = usuario.persona_ID,
        nombre_usuario=usuario.nombre_usuario,
        correo_electronico=usuario.correo_electronico,
        numero_telefono_movil=usuario.numero_telefono_movil,
        contrasenia=hashed_password,  # Guarda la contraseña encriptada
        estatus=usuario.estatus
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def registrar_usuario(db: Session, usuario: schemas.UsuarioCreate):
    try:
        # 1. Hashear la contraseña
        hashed_password = hash_password(usuario.contrasenia)
        
        # 2. Crear instancia del usuario
        db_usuario = Usuario(
            persona_ID=usuario.persona_ID,
            nombre_usuario=usuario.nombre_usuario,
            correo_electronico=usuario.correo_electronico,
            numero_telefono_movil=usuario.numero_telefono_movil,
            contrasenia=hashed_password,
            estatus=usuario.estatus
        )
        db.add(db_usuario)
        db.flush()  # Genera el ID sin hacer commit
        
        # 3. Obtener o crear rol "Usuario" (manejo robusto)
        rol = obtener_rol_por_nombre(db, nombre_rol="Usuario")
        if not rol:
            rol = crear_rol_predeterminado(db, nombre_rol="Usuario")
        
        # 4. Asignar rol al usuario
        db_usuarios_roles = UsuarioRol(
            usuario_ID=db_usuario.id,
            rol_ID=rol.id
        )
        db.add(db_usuarios_roles)
        
        # 5. Commit final (todo o nada)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
        
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Error de integridad: Posible duplicidad de datos."
        )
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Error interno al registrar el usuario."
        )
        
        
def actualizar_usuario(db: Session, id: int, usuario: schemas.UsuarioUpdate):
    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if db_usuario:
        for var, value in vars(usuario).items():
            setattr(db_usuario, var, value) if value else None
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def eliminar_usuario(db: Session, id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario
