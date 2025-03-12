from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger
from config.db import Base


class UsuarioDirecciones(Base):
    __tablename__ = "tbd_usuario_direcciones"

    usuario_ID =  Column(Integer, ForeignKey("tbb_usuario.id"),  primary_key=True)
    direccion_ID =  Column(Integer, ForeignKey("tbb_direcciones.id"))
    estatus = (Column(SmallInteger))
    fecha_registro = Column(DateTime, default=datetime)
    fecha_actualizacion = Column(DateTime, default=datetime)
    