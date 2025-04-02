from datetime import date
from typing import Literal
from pydantic import BaseModel


class CitasBase(BaseModel):

    estatus : Literal[0, 1]
    fecha_inicio : date
    fecha_fin : date
    servicio_ID : int
    usuario_ID : int

class CitasCreate(CitasBase):
    pass

class CitasUpdate(CitasBase):
    pass

class Citas(CitasBase):
    id : int
    class Config:
        orm_mode = True