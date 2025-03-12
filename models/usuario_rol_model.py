from sqlalchemy import Column, ForeignKey, Integer
from config.db import Base


class UsuarioRol(Base):
    __tablename__ = "tbd_usuario_rol"
    usuario_ID =  Column(Integer, ForeignKey("tbb_usuario.id"),  primary_key=True)
    rol_ID =  Column(Integer, ForeignKey("tbb_rol.id"))