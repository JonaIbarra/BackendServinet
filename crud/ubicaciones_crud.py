from requests import Session
from models.ubicaciones_model import Ubicaciones
from schemas import ubicaciones_schema as schemas


def obtener_todas_las_ubicaciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ubicaciones).offset(skip).limit(limit).all()

def obtener_ubicacion_por_ID(db: Session, id: int):
    return db.query(Ubicaciones).filter(Ubicaciones.id == id).first()

def obtener_ubicacion_por_direccion(db: Session, pais: str, estado: str, ciudad: str, colonia: str,
                                    calle: str, numero_exterior: str, codigo_postal: str):
    return db.query(Ubicaciones).filter(
        Ubicaciones.pais == pais,
        Ubicaciones.estado == estado,
        Ubicaciones.ciudad == ciudad,
        Ubicaciones.colonia == colonia,
        Ubicaciones.calle == calle,
        Ubicaciones.numero_exterior == numero_exterior,
        Ubicaciones.codigo_postal == codigo_postal
    ).first()

def crear_ubicacion(db: Session, ubicaciones: schemas.UbicacionesCreate):
    db_ubicaciones = Ubicaciones(**ubicaciones.dict())
    db.add(db_ubicaciones)
    db.commit()
    db.refresh(db_ubicaciones)
    return db_ubicaciones

def actualizar_ubicaciones(db: Session, id: int, ubicaciones: schemas.UbicacionesUpdate):    
    db_ubicaciones = db.query(Ubicaciones).filter(Ubicaciones.id == id).first()
    if db_ubicaciones:
        for var, value in vars(ubicaciones).items():
            setattr(db_ubicaciones, var, value) if value else None
        db.commit()
        db.refresh(db_ubicaciones)
    return db_ubicaciones

def eliminar_ubicaciones(db: Session, id: int):
    db_ubicaciones = db.query(Ubicaciones).filter(Ubicaciones.id == id).first()
    if db_ubicaciones:
        db.delete(db_ubicaciones)
        db.commit()
    return db_ubicaciones
