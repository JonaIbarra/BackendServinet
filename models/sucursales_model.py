from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String
from config.db import Base

class Sucursales(Base):
    __tablename__ = "tbb_sucursales"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255))
    empresa = Column(String(255))
    telefono = Column(String(45))
    correo_electronico = Column(String(255))
    estatus = Column(SmallInteger)
    fecha_registro = Column(DateTime, default=datetime)
    fecha_ultima_actualizacion = Column(DateTime, default=datetime)
    horario_ID = Column(Integer, ForeignKey("tbb_horarios.id"))
    ubicacion_ID = Column(Integer, ForeignKey("tbb_ubicaciones.id"))
    