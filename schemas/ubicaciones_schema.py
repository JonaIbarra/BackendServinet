from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class UbicacionesBase(BaseModel):

    pais: str
    estado: str
    ciudad: str
    colonia: str
    calle: str
    numero_exterior: str
    numero_interior: str
    codigo_postal: str
    estatus: Literal[0, 1]
    referencias: str


class UbicacionesCreate(UbicacionesBase):
    pass

class UbicacionesUpdate(UbicacionesBase):
    pass

class Ubicaciones(UbicacionesBase):
    
    id: int
    class Config:
        orm_mode = True
        