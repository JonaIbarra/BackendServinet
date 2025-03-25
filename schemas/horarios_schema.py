from datetime import datetime, time
from typing import Literal
from pydantic import BaseModel
from models.horarios_model import DiasEnum


class HorariosBase(BaseModel):

    dia_semana: DiasEnum
    hora_apertura: time
    hora_cierre: time
    es_cerrado: Literal[0, 1]
    estatus: Literal[0, 1]


    


class HorariosCreate(HorariosBase):
    pass

class HorariosUpdate(HorariosBase):
    pass

class Horarios(HorariosBase):
    id : int
    class Config:
        orm_mode = True
    
