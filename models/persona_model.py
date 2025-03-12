from datetime import datetime
import enum  
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Date, DateTime, Integer, SmallInteger, String, func, Enum
from config.db import Base


class TipoPersonaEnum(str, enum.Enum):
    Moral = "Moral"
    Fisica = "Fisica"

class Personas(Base):
    __tablename__ = "tbb_persona"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tipo = Column(Enum(TipoPersonaEnum, values_callable=lambda x: [e.value for e in x]), nullable=False)  
    rfc = Column(String(13), nullable=False, unique=True)
    estatus = Column(SmallInteger, nullable=False)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())

     # Relaciones (1:1)
    persona_fisica = relationship("Personas_Fisicas", back_populates="persona", uselist=False)
    persona_moral = relationship("Personas_Moral", back_populates="persona", uselist=False)


