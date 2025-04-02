from sqlalchemy import Column, DateTime, ForeignKey, Integer, func
from config.db import Base


class UsuarioRol(Base):
    __tablename__ = "tbd_usuario_rol"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_ID =  Column(Integer, ForeignKey("tbb_usuario.id"),  primary_key=True)
    rol_ID =  Column(Integer, ForeignKey("tbb_rol.id"))
    fecha_registro = Column(DateTime, default=func.now())
    fecha_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())