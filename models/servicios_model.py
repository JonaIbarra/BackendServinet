from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, SmallInteger, String

from config.db import Base


class Servicios(Base):
    __tablename__ = "tbb_servicios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255))
    descripcion = Column(String(255))
    duracion = Column(Integer)
    precio = Column(Float)
    estatus = Column(SmallInteger)
    tipo_servicio = Column(String(45))
    fecha_registro = Column(DateTime, default=datetime)
    fecha_actualizacion = Column(DateTime, default=datetime)
    usuario_ID = Column(Integer, ForeignKey("tbb_usuario.id"))
    sucursal_ID = Column(Integer, ForeignKey("tbb_sucursales.id"))
