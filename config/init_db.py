from sqlalchemy.orm import Session
from models.rol_model import Rol
from config.db import engine, SessionLocal

# Lista de roles predefinidos
ROLES_PREDEFINIDOS = [
    {"nombre_rol": "admin", "descripcion": "Administrador del sistema"},
    {"nombre_rol": "usuario", "descripcion": "Usuario estándar"},
    {"nombre_rol": "moderador", "descripcion": "Usuario con permisos de moderación"}
]

def initialize_roles(db: Session):
    """
    Verifica si los roles predefinidos existen en la base de datos.
    Si no existen, los crea automáticamente.
    """
    for role_data in ROLES_PREDEFINIDOS:
        existing_role = db.query(Rol).filter(Rol.nombre_rol == role_data["nombre_rol"]).first()
        if not existing_role:
            new_role = Rol(**role_data)
            db.add(new_role)
    db.commit()

def init_db():
    """
    Se encarga de inicializar la base de datos y poblar los roles.
    """
    db = SessionLocal()
    try:
        initialize_roles(db)
    finally:
        db.close()

