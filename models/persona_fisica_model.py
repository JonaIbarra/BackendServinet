from datetime import datetime
import enum
from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, String, Boolean, DateTime, Enum, Date, func
from sqlalchemy.orm import relationship
from config.db import Base



class GeneroEnum(str, enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"


class Personas_Fisicas(Base):
    __tablename__ = "tbb_persona_fisica"

    persona_ID = Column(Integer, ForeignKey("tbb_persona.id"), primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=False)
    genero = Column(Enum(GeneroEnum, values_callable=lambda x: [e.value for e in x]), nullable=False)  
    curp = Column(String(18), nullable=False, unique=True)
    titulo_cortesia = Column(String(10), nullable=False)
    direccion = Column(String(255), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)  # Corrige typo "feca_nacimiento"
    estatus = Column(SmallInteger, nullable=False)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_ultima_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())  # Corrige "fecha__ultima..."

    persona = relationship("Personas", back_populates="persona_fisica")







