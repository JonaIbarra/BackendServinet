from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, func
from config.db import Base

class Sucursales(Base):
    __tablename__ = "tbb_sucursales"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(10), nullable=False)
    correo = Column(String(50), nullable=False)
    ubicacion_id = Column(Integer, ForeignKey("tbb_ubicaciones.id"), nullable=False)
    horario_id = Column(Integer, ForeignKey("tbb_horarios.id"), nullable=False)
    fecha_creacion = Column(DateTime, default=func.now())
    fecha_modificacion = Column(DateTime, default=func.now())
    estatus = Column(SmallInteger, default=1)
    