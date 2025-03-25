from datetime import datetime
from enum import Enum
from typing import Union
from pydantic import BaseModel
from schemas.persona_fisica_schema import PersonaFisicaCreate
from schemas.persona_moral_schema import PersonaMoralCreate

class TipoPersonaEnum(str, Enum):
    Moral = "Moral"
    Fisica = "Fisica"

class PersonaBase(BaseModel):
    rfc: str
    estatus: int 


# Esquema combinado para el formulario
class PersonaCreate(BaseModel):
    tipo: TipoPersonaEnum
    datos_generales: PersonaBase
    datos_especificos: Union[PersonaFisicaCreate, PersonaMoralCreate]

class PersonaUpdate(PersonaBase):
    pass

class Persona(PersonaBase):
    id: int
    tipo: str
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        from_attributes = True  
        use_enum_values = True  