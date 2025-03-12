from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la conexión a la base de datos
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_EKDs0CiGYRqSrfjYO6j@backendservinet-animateibarra97-5f64.g.aivencloud.com/defaultdb"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)


# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión de base de datos
Base = declarative_base()
