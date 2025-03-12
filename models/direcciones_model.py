from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String
from config.db import Base


class Direcciones(Base):
    __tablename__ = "tbb_direcciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tipo = Column(String(100))
    valor = Column(String(250))
    estatus = Column(SmallInteger)
    fecha_registro = Column(DateTime, default=datetime)
    fecha_actualizacion = Column(DateTime, default=datetime)
    ID_superior = Column(Integer)


