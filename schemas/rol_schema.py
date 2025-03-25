from datetime import datetime
from pydantic import BaseModel


class RolBase(BaseModel):

    nombre_rol : str
    descripcion : str

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    id : int
    class Config:
        orm_mode =  True

