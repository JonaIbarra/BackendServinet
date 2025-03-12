from datetime import datetime, timedelta
from typing import Optional
import jwt  # PyJWT
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
# from fastapi.security import OAuth2PasswordBearer
from jwt import encode, decode

# Configurar el contexto de encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Función para encriptar contraseñas
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Función para verificar contraseñas
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)




def solicita_token (dato:dict)->str:
    token:str=encode(payload=dato,key='mi_clave',algorithm='HS256')
    return token
def valida_token(token:str)->dict:
    dato:dict = decode(token,key='mi_clave',algorithms=['HS256'])
    return dato
