

from typing import Literal
from pydantic import BaseModel


class CanjesBase(BaseModel):
    costo_puntos_lealtad: int
    observaciones: str
    estatus: Literal[0, 1] = 1
    usuario_ID: int
    cita_ID: int
    

class CanjesCreate(CanjesBase):
    pass

class CanjesUpdate(CanjesBase):
    pass

class Canjes(CanjesBase):
    id: int
    class Config:
        orm_mode = True