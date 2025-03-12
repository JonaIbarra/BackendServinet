from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class CancelacionesBase(BaseModel):
    id: int
    usuario_solicitante: int
    usuario_aprueba: int
    estatus: Literal[0, 1]
    motivo: str
    fecha_registro: datetime
    fecha_ultima_actualizacion: datetime
    cita_ID: int
    servicio_ID: int

class CancelacionesCreate(CancelacionesBase):
    pass

class CancelacionesUpdate(CancelacionesBase):
    pass

class Cancelaciones(CancelacionesBase):
    class Config:
        
        orm_mode = True