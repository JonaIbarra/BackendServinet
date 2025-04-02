from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class CancelacionesBase(BaseModel):

    usuario_solicitante: int
    usuario_autorizador: int
    estatus: Literal[0, 1] = 1
    motivo: str
    cita_ID: int
    servicio_ID: int

class CancelacionesCreate(CancelacionesBase):
    pass

class CancelacionesUpdate(CancelacionesBase):
    pass

class Cancelaciones(CancelacionesBase):
    id: int
    class Config:
        orm_mode = True