from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la conexión a la base de datos
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_g-tqDl-Sn2nan3BXlnj@mysql-22a90db5-e19063584-e1b0.g.aivencloud.com:22520/defaultdb?ssl_mode=REQUIRED"


# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)


# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión de base de datos
Base = declarative_base()
