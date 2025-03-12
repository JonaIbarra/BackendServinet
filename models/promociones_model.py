from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String
from config.db import Base

class Promociones(Base):
    __tablename__ = "tbb_promociones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(255))
    descripcion = Column(String(255))
    relacion = Column(String(255))
    tipo = Column(String(255))
    estatus = Column(SmallInteger)
    hora_inicio = Column(DateTime, default=datetime)
    hora_fin = Column(DateTime, default=datetime)
    fecha_registro = Column(DateTime, default=datetime)
    fecha_ultima_actualizacion = Column(DateTime, default=datetime)
    servicio_ID = Column(Integer, ForeignKey("tbb_servicios.id"))
