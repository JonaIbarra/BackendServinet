
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, SmallInteger, func

from config.db import Base


class Citas(Base):
    __tablename__ = "tbb_citas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    estatus = Column(SmallInteger)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())
    usuario_ID = Column(Integer, ForeignKey("tbb_usuario.id"))
    servicio_ID = Column(Integer, ForeignKey("tbb_servicios.id"))