from datetime import datetime
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel


class ServiciosBase(BaseModel):

    nombre: str
    descripcion: str
    precio: float
    duracion: Decimal
    precio: float
    tipo_servicio: str 
    fecha_registro: datetime
    fecha_actualizacion: datetime
    estatus: Literal[0, 1]
    sucursal_id: int
    categoria_id: int
    



class ServiciosCreate(ServiciosBase):
    pass

class ServiciosUpdate(ServiciosBase):
    pass

class Servicios(ServiciosBase):
    
    class Config:
        usuario_ID : int
        orm_mode = True