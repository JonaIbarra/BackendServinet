from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String, DECIMAL
from config.db import Base


class Ubicaciones(Base):
    __tablename__ = "tbb_ubicaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pais = Column(String(45))
    estado = Column(String(45))
    ciudad = Column(String(45))
    colonia = Column(String(45))
    calle = Column(String(45))
    numero_exterior = Column(String(10))
    numero_interior = Column(String(10))
    codigo_postal = Column(String(10))
    latitud = Column(DECIMAL(10,8))
    longitud = Column(DECIMAL(11,8))
    estatus = Column(SmallInteger)
    fecha_registro = Column(DateTime, default=datetime.now())
    fecha_ultima_actualizacion = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    referencias = Column(String(255))
    