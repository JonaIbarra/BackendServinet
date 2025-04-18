import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# OJO: Elimina ?ssl_mode=REQUIRED de la URL porque pymysql NO lo soporta
DATABASE_URL = os.getenv("AIVEN_DATABASE_URI")
# Crear el motor de la base de datos con el argumento SSL
engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {}}
)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarativa base
Base = declarative_base()











