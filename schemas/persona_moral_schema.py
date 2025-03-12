from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class PersonaMoralBase(BaseModel):
    razon_social : str
    direccion : str
    estatus : int
    

class PersonaMoralCreate(PersonaMoralBase):
    pass

class PersonaMoralUpdate(PersonaMoralBase):
    pass



class PersonaMoral(PersonaMoralBase):
    class Config:
        orm_mode = True