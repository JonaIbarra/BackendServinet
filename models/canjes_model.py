from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, func
from config.db import Base


class Canjes(Base):
    __tablename__ = "tbb_canjes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    costo_puntos_lealtad = Column(Integer)
    observaciones = Column(String(255))
    estatus = Column(SmallInteger)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_ultima_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())
    usuario_ID = Column(Integer, ForeignKey("tbb_usuario.id"))
    cita_ID = Column(Integer, ForeignKey("tbb_citas.id"))