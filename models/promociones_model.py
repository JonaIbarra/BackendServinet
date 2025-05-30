from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, func
from config.db import Base

class Promociones(Base):
    __tablename__ = "tbb_promociones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(255))
    descripcion = Column(String(255))
    relacion = Column(String(255))
    tipo = Column(String(255))
    estatus = Column(SmallInteger)
    hora_inicio = Column(DateTime)
    hora_fin = Column(DateTime)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_ultima_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())
    servicio_ID = Column(Integer, ForeignKey("tbb_servicios.id"))
