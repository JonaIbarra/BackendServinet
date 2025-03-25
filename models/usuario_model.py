from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, func
from config.db import Base


class Usuario(Base):
    __tablename__ = "tbb_usuario"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    persona_ID =  Column(Integer, ForeignKey("tbb_persona.id"))
    nombre_usuario = Column(String(30))
    correo_electronico = Column(String(100))
    numero_telefono_movil = Column(String(10))
    contrasenia = Column(String(300))
    estatus = Column(SmallInteger)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_ultimo_acceso = Column(DateTime, default=func.now(), onupdate=func.now())

