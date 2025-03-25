from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, func
from config.db import Base

class Rol(Base):
    __tablename__ = "tbb_rol"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_rol = Column(String(25))
    descripcion = Column(String(200))
    fecha_registro = Column(DateTime, default=func.now())
    fecha_ultima_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())
