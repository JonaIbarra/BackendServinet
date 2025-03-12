from datetime import datetime
from pydantic import BaseModel


class CategoriasBase(BaseModel):
    id: int
    nombre: str
    estatus: int
    descripcion: str
    categoria_superior: int
    fecha_registro: datetime
    fecha_ultima_actualizacion: datetime
    servicio_ID: int


class CategoriasCreate(CategoriasBase):
    pass

class CategoriasUpdate(CategoriasBase): 
    pass

class Categorias(CategoriasBase):
    class Config:
        orm_mode = True
        servicio_ID: int
