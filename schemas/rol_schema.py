from datetime import datetime
from pydantic import BaseModel


class RolBase(BaseModel):
    id : int
    nombre_rol : str
    descripcion : str
    fecha_registro : datetime
    fecha_ultima_actualizacion : datetime

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    class Config:
        orm_mode =  True

