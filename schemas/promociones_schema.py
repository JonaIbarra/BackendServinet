from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class PromocionesBase(BaseModel):
   
    titulo: str
    descripcion: str
    relacion: str
    tipo: str
    estatus: Literal[0, 1]
    hora_inicio: datetime
    hora_fin: datetime
    servicio_ID: int

class PromocionesCreate(PromocionesBase):
    pass

class   PromocionesUpdate(PromocionesBase):
    pass


class Promociones(PromocionesBase):
    id: int
    class Config:
        orm_mode = True
        