from sqlalchemy.orm import Session
from models.usuario_model import Usuario
from schemas import usuario_schema as schemas
from services.auth import hash_password


def obtener_todos_los_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()

def obtener_usuario_por_ID(db: Session, id: int):
    return db.query(Usuario).filter(Usuario.id == id).first()

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
        fecha_registro=usuario.fecha_registro,
        fecha_ultimo_acceso=usuario.fecha_ultimo_acceso,
        estatus=usuario.estatus
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

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
