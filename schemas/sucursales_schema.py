from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class SucursalesBase(BaseModel):
    id : int
    nombre : str
    empresa : str
    telefono : str
    correo_electronico : str
    estatus : Literal[0, 1]
    fecha_registro : datetime
    fecha_ultima_actualizacion : datetime
    horario_ID: int
    ubicacion_ID: int

class SucursalesCreate(SucursalesBase):
    pass

class SucursalesUpdate(SucursalesBase):
    pass

class Sucursales(SucursalesBase):
    class Config:
        orm_mode = True
        horario_ID: int
        ubicacion_ID: int
