from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String
from config.db import Base


class Categorias(Base):
    __tablename__ = "tbb_categorias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255))
    estatus = Column(SmallInteger)
    descripcion = Column(String(255))
    categoria_superor = Column(Integer)
    fecha_registro = Column(DateTime, default=datetime)
    fecha_ultima_actualizacion = Column(DateTime, default=datetime)
    servicio_ID = Column(Integer, ForeignKey("tbb_servicios.id"))
    
