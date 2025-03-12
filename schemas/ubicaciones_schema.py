from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class UbicacionesBase(BaseModel):
    id: int
    codigo_postal: str
    calle: str
    numero: str
    colonia: str
    referencia: str
    contacto: str
    estatus: Literal[0, 1] 
    fecha_registro: datetime
    fecha_ultima_actualizacion: datetime

class UbicacionesCreate(UbicacionesBase):
    pass

class UbicacionesUpdate(UbicacionesBase):
    pass

class Ubicaciones(UbicacionesBase):

    class Config:
        orm_mode = True
        