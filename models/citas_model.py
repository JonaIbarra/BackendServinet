from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger

from config.db import Base


class Citas(Base):
    __tablename__ = "tbb_citas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_ID = Column(Integer, ForeignKey("tbb_usuario.id"))
    estatus = Column(SmallInteger)
    servicio_ID = Column(Integer, ForeignKey("tbb_servicios.id"))
    fecha_registro = Column(DateTime, default=datetime)
    fecha_actualizacion = Column(DateTime, default=datetime)
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)