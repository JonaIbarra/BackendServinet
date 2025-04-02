import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException
import jwt  # PyJWT
from passlib.context import CryptContext

# Cargar las variables desde el archivo .env
load_dotenv()

# Obtener valores del .env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Configurar el contexto de encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Función para encriptar contraseñas
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Función para verificar contraseñas
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Función para generar un token JWT
def solicita_token(dato: dict) -> str:
    """Genera un token JWT con expiración"""
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dato.update({"exp": expire})  # Agregar tiempo de expiración al token
    token = jwt.encode(payload=dato, key=SECRET_KEY, algorithm=ALGORITHM)
    return token

# Función para validar un token JWT
def valida_token(token: str) -> dict:
    """Decodifica un token JWT y verifica su validez"""
    try:
        dato = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return dato
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
