from datetime import datetime, time
from typing import Literal
from pydantic import BaseModel


class HorariosBase(BaseModel):
    id : int
    dia : str
    hora_inicio : datetime
    hora_fin : datetime
    estatus : Literal[0, 1]
    descripcion : str
    fecha_registro : datetime
    fecha_ultima_actualizacion : datetime
    horario_apertura : time
    horario_cierre : time


class HorariosCreate(HorariosBase):
    pass

class HorariosUpdate(HorariosBase):
    pass

class Horarios(HorariosBase):
    class Config:
        orm_mode = True
        horario_apertura : time
        horario_cierre : time
