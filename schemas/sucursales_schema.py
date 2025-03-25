from datetime import datetime
from typing import Literal
from pydantic import BaseModel

from schemas.horarios_schema import HorariosCreate
from schemas.ubicaciones_schema import UbicacionesCreate


class SucursalesBase(BaseModel):


    nombre: str
    telefono: str
    correo: str
    estatus: Literal[0, 1]
    
    


class SucursalesCreate(BaseModel):
    datos_sucursal: SucursalesBase
    datos_horario: HorariosCreate
    datos_ubicacion: UbicacionesCreate


class SucursalesUpdate(SucursalesBase):
    pass

class Sucursales(SucursalesBase):
    
    id: int
    class Config:
        orm_mode = True
      
