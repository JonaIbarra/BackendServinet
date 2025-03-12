from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String
from config.db import Base


class Medio_Contactos(Base):
    __tablename__ = "tbb_medio_contactos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario = Column(String(45))
    descripcion = Column(String(255))
    tipo_contacto = Column(String(45))
    valor_contacto = Column(String(45))
    estatus = Column(SmallInteger)
    fecha_registro = Column(DateTime, default=datetime)
    fecha_ultima_actualizacion = Column(DateTime, default=datetime)
    servicio_ID = Column(Integer, ForeignKey("tbb_servicios.id"))