from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class PromocionesBase(BaseModel):
    id: int
    titulo: str
    descripcion: str
    relacion: str
    tipo: str
    estatus: Literal[0, 1]
    hora_inicio: datetime
    hora_fin: datetime
    fecha_registro: datetime
    fecha_ultima_actualizacion: datetime
    servicio_ID: int

class PromocionesCreate(PromocionesBase):
    pass

class   PromocionesUpdate(PromocionesBase):
    pass


class Promociones(PromocionesBase):
    
    class Config:
        orm_mode = True
        