from pydantic import BaseModel


class UsuarioRolBase(BaseModel):
    usuario_ID : int
    rol_ID : int


class UsuarioRol(UsuarioRolBase):
    class Config:
        orm_mode = True
        usuario_ID : int
        rol_ID : int