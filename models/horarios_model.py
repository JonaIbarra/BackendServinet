from datetime import datetime
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, SmallInteger, String, Time, Enum
from config.db import Base
import enum

    
class DiasEnum(str, enum.Enum):
    Lunes = "Lunes"
    Martes = "Martes"
    Miercoles = "Miercoles"
    Jueves = "Jueves"
    Viernes = "Viernes"
    Sabado = "Sabado"
    Domingo = "Domingo"



class Horarios(Base):
    __tablename__ = "tbb_horarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dia_semana = Column(Enum(DiasEnum, values_callable=lambda x: [e.value for e in x]), nullable=False)  
    hora_apertura = Column(Time, nullable=False)
    hora_cierre = Column(Time, nullable=False)
    sucursal_id = Column(Integer, ForeignKey("tbb_sucursales.id"), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now())
    fecha_modificacion = Column(DateTime, default=datetime.now())
    es_cerrado = Column(SmallInteger, default=0)
    estatus = Column(SmallInteger, default=1)
    
    
    
    
