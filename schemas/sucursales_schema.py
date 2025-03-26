from datetime import datetime
from typing import Literal
from pydantic import BaseModel

import schemas.horarios_schema as schemas
from schemas.ubicaciones_schema import UbicacionesCreate


class SucursalesBase(BaseModel):


    nombre: str
    telefono: str
    correo: str
    estatus: Literal[0, 1]
    
    


class SucursalesCreate(BaseModel):
    datos_sucursal: SucursalesBase
    datos_ubicacion: UbicacionesCreate
    # Horarios para cada día
    lunes: schemas.HorariosCreateLunes
    martes: schemas.HorariosCreateMartes
    miercoles: schemas.HorariosCreateMiercoles
    jueves: schemas.HorariosCreateJueves
    viernes: schemas.HorariosCreateViernes
    sabado: schemas.HorariosCreateSabado
    domingo: schemas.HorariosCreateDomingo

class SucursalesUpdate(SucursalesBase):
    pass

class Sucursales(SucursalesBase):
    
    id: int
    class Config:
        orm_mode = True
      
