from pydantic import BaseModel


class UsuarioRolBase(BaseModel):
    usuario_ID : int
    rol_ID : int
    
class UsuarioRolCreate(UsuarioRolBase):
    pass

class UsuarioRolUpdate(UsuarioRolBase):
    rol_ID : int


class UsuarioRol(UsuarioRolBase):
    id : int
    class Config:
        orm_mode = True