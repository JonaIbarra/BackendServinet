from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String
from config.db import Base


class Ubicaciones(Base):
    __tablename__ = "tbb_ubicaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo_postal = Column(String(5))
    calle = Column(String(255))
    numero = Column(String(45))
    colonia = Column(String(45))
    referencia = Column(String(255))
    contacto = Column(String(45))
    estatus = Column(SmallInteger)
    fecha_registro = Column(DateTime, default=datetime)
    fecha_ultima_actualizacion = Column(DateTime, default=datetime)
    