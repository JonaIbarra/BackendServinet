from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class ServiciosBase(BaseModel):
    id : int
    nombre : str
    descripcion : str
    duracion : int
    precio : float
    estatus : int
    estatus : Literal[0, 1] 
    tipo_servicio : str
    fecha_registro : datetime
    fecha_actualizacion : datetime
    usuario_ID : int
    sucursal_ID : int


class ServiciosCreate(ServiciosBase):
    pass

class ServiciosUpdate(ServiciosBase):
    pass

class Servicios(ServiciosBase):
    
    class Config:
        usuario_ID : int
        orm_mode = True