from datetime import datetime
from sqlalchemy import Column, Date, DateTime, Integer, SmallInteger, String, Time
from config.db import Base


class Horarios(Base):
    __tablename__ = "tbb_horarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dia = Column(Date)
    hora_inicio = Column(DateTime)
    hora_fin = Column(DateTime)
    estatus = Column(SmallInteger)
    descripcion = Column(String(255))
    fecha_registro = Column(DateTime, default=datetime)
    fecha_ultima_actualizacion = Column(DateTime, default=datetime)
    horario_apertura = Column(Time)
    horario_apertura = Column(Time)