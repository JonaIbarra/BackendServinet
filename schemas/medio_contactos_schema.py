from datetime import datetime
from pydantic import BaseModel


class MedioContactosBase(BaseModel):
    id: int
    usuario: str
    descripcion: str
    tipo_contacto: str
    valor_contacto: str
    estatus: int
    fecha_registro: datetime
    fecha_ultima_actualizacion: datetime
    servicio_ID: int


class  MedioContactosCreate(MedioContactosBase):
    pass

class  MedioContactosUpdate(MedioContactosBase):
    pass

class MedioContactos(MedioContactosBase):
    
    class Config:
        orm_mode = True
        servicio_ID: int

