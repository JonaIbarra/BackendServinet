from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, Numeric, SmallInteger, String, Text

from config.db import Base


class Servicios(Base):
    __tablename__ = "tbb_servicios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    precio = Column(Float, nullable=False)
    duracion = Column(Numeric(10,2), nullable=False)
    precio = Column(Float, nullable=False)
    tipo_servicio = Column(String(50), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now())
    fecha_actualizacion = Column(DateTime, default=datetime.now())
    estatus = Column(SmallInteger, default=1)
    sucursal_id = Column(Integer, ForeignKey("tbb_sucursales.id"), nullable=False)
    