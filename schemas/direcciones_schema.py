from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class DireccionesBase(BaseModel):
    
    id : int
    tipo : str
    valor : str
    estatus : Literal[0, 1]
    fecha_registro : datetime
    fecha_actualizacion : datetime
    ID_superior : int

class DireccionesCreate(DireccionesBase):
    pass

class DireccionesUpdate(DireccionesBase):
    pass

class Direcciones(DireccionesBase):
    class Config:
        orm_mode = True

