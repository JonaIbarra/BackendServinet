from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, func
from config.db import Base
from sqlalchemy.orm import relationship


class Personas_Moral(Base):
    __tablename__ = "tbb_persona_moral"

    persona_ID = Column(Integer, ForeignKey("tbb_persona.id"), primary_key=True)
    razon_social = Column(String(45))
    direccion = Column(String(100))
    estatus = Column(SmallInteger, nullable=False)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_ultima_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())

    persona = relationship("Personas", back_populates="persona_moral")


