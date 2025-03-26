from datetime import datetime, time
from typing import Literal
from pydantic import BaseModel
from models.horarios_model import DiasEnum


class HorariosBase(BaseModel):

    dia_semana: DiasEnum
    hora_apertura: time
    hora_cierre: time
    es_cerrado: Literal[0, 1] = 0
    estatus: Literal[0, 1] = 1


    


class HorariosCreateLunes(HorariosBase):
    dia_semana: DiasEnum = DiasEnum.Lunes
    pass

class HorariosCreateMartes(HorariosBase):
    dia_semana: DiasEnum = DiasEnum.Martes
    pass

class HorariosCreateMiercoles(HorariosBase):    
    dia_semana: DiasEnum = DiasEnum.Miercoles
    pass

class HorariosCreateJueves(HorariosBase):
    dia_semana: DiasEnum = DiasEnum.Jueves
    pass

class HorariosCreateViernes(HorariosBase):
    dia_semana: DiasEnum = DiasEnum.Viernes
    pass

class HorariosCreateSabado(HorariosBase):
    dia_semana: DiasEnum = DiasEnum.Sabado
    pass

class HorariosCreateDomingo(HorariosBase):
    dia_semana: DiasEnum = DiasEnum.Domingo
    pass


class HorariosUpdate(HorariosBase):
    pass

class Horarios(HorariosBase):
    id : int
    class Config:
        orm_mode = True
    
