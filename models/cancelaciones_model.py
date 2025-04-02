from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, func
from config.db import Base


class Cancelaciones(Base):
    __tablename__ = "tbb_cancelaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_solicitante = Column(Integer, ForeignKey("tbb_usuario.id"))
    usuario_autorizador = Column(Integer, ForeignKey("tbb_usuario.id"))
    estatus = Column(SmallInteger)
    motivo = Column(String(255))    
    fecha_registro = Column(DateTime, default=func.now())
    fecha_ultima_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())
    cita_ID = Column(Integer, ForeignKey("tbb_citas.id"))
    servicio_ID = Column(Integer, ForeignKey("tbb_servicios.id"))
