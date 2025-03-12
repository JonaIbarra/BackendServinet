from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class UsuariosDireccionesBase(BaseModel):
    id : int
    usuario_ID : int
    direccion_ID : int
    estatus : Literal[0, 1]
    fecha_registro : datetime
    fecha_actualizacion : datetime


class UsuariosDireccionesCreate(UsuariosDireccionesBase):
    pass

class UsuariosDireccionesUpdate(UsuariosDireccionesBase):
    pass

class UsuariosDirecciones(UsuariosDireccionesBase):
    class Config:
        usuario_ID : int
        direccion_ID : int
        orm_mode = True
    