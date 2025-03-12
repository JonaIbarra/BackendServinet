from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class CitasBase(BaseModel):
    id : int
    usuario_ID : int
    estatus : Literal[0, 1]
    servicio_ID : int
    fecha_registro : datetime
    fecha_actualizacion : datetime
    fecha_inicio : datetime
    fecha_fin : datetime

class CitasCreate(CitasBase):
    pass

class CitasUpdate(CitasBase):
    pass

class Citas(CitasBase):
    class Config:
        usuario_ID : int
        servicio_ID : int
        orm_mode = True