from datetime import date, datetime
import enum
from typing import Literal
from pydantic import BaseModel, field_validator
from models.persona_fisica_model import GeneroEnum




class PersonaFisicaBase(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    genero: GeneroEnum
    curp: str
    titulo_cortesia: str
    direccion: str
    fecha_nacimiento: date
    estatus: int


class PersonaFisicaCreate(PersonaFisicaBase):
    pass

    @field_validator('fecha_nacimiento')
    def validar_mayoria_edad(cls, fecha_nacimiento: date) -> date:
        hoy = date.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        
        if edad < 18:
            raise ValueError("Debe ser mayor de edad (18 años o más)")
        
        return fecha_nacimiento

class PersonaFisicaUpdate(PersonaFisicaBase):
    pass
 
class PersonaFisica(PersonaFisicaBase):
    class Config:
    
        orm_mode = True









