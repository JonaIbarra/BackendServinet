from datetime import datetime
from typing import Literal
from pydantic import BaseModel



class UsuarioLogin(BaseModel):
    campo_login: str  # Puede ser: correo, teléfono o nombre_usuario
    contrasenia: str



class UsuarioBase(BaseModel):
 
    persona_ID : int
    nombre_usuario : str
    correo_electronico : str
    numero_telefono_movil : str
    contrasenia : str
    estatus : Literal[0, 1] = 1





class UsuarioCreate(UsuarioBase):
        pass

class UsuarioUpdate(UsuarioBase):
        pass

class Usuario(UsuarioBase):
    class Config:
        id : int
        persona_ID : int
        orm_mode = True
