from datetime import datetime
from pydantic import BaseModel


class CategoriasBase(BaseModel):

    nombre: str
    estatus: int
    descripcion: str
    categoria_superior: int




class CategoriasCreate(CategoriasBase):
    pass

class CategoriasUpdate(CategoriasBase): 
    pass

class Categorias(CategoriasBase):
    id: int
    class Config:
        orm_mode = True
        
