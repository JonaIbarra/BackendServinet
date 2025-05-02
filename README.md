```markdown
# API con FastAPI, PostgreSQL/MySQL y Autenticación JWT

API moderna con autenticación segura, operaciones CRUD y arquitectura escalable usando tecnologías Python.

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

## 🛠️ Tecnologías Clave

### **Backend**
- FastAPI 0.114.0
- Uvicorn 0.30.1
- SQLAlchemy 2.0.31

### **Seguridad**
- Bcrypt 4.2.1
- PyJWT 2.8.0
- Passlib 1.7.4

### **Base de Datos**
- MySQL/PostgreSQL

### **Utilidades**
- Pydantic 2.7.4 (validación)
- Python-dotenv 1.0.1

## ⚙️ Requisitos

- Python 3.10+
- MySQL 8+ o PostgreSQL 14+
- Pip 23+
- Git 2.38+

## 🚀 Instalación Rápida

1. **Clonar repositorio y configurar entorno**
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd BackendServiNet
:: Crear entorno virtual
python -m venv .venv

:: Activar entorno
.venv\Scripts\activate.bat
```


```powershell
# Crear entorno
python -m venv .venv

# Activar
.\.venv\Scripts\Activate.ps1
```




2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno**
Crear archivo `.env` con:
```env
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=mysql://usuario:contraseña@localhost:3306/nombre_bd
```

4. **Iniciar servidor**
```bash
uvicorn app.main:app --reload
```

## 🔒 Autenticación JWT

Ejemplo de ruta protegida:
```python
from fastapi import Depends

@categorias_routes.post("/categorias", 
                      response_model=schemas.Categorias, 
                      dependencies=[Depends(Portador())])
async def crear_categoria(categoria: schemas.CategoriaCreate):
    # Lógica del endpoint
    return ...
```

### Funcionamiento de la autenticación:
1. Cliente envía credenciales a `/login`
2. Servidor valida y devuelve JWT

## EJEMPLO Login (Obtener JWT):
```http
http
POST /auth/login
Content-Type: application/json

{
  "email": "usuario@servinet.com",
  "password": "SecurePass123!"
}

# Respuesta
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
 ```

## 📌 Características Principales

- Registro y autenticación de usuarios
- CRUD completo con validación Pydantic
- Modelos de base de datos con SQLAlchemy ORM
- Configuración centralizada con variables de entorno
- Documentación interactiva (Swagger UI en `/docs`)


## 🔒 Características de Seguridad
- Autenticación JWT con tiempo de expiración
- Hashing de contraseñas con bcrypt
- Validación de tokens en cada solicitud protegida
- Esquemas de validación Pydantic para todos los endpoints
- Variables sensibles en archivo .env
- Protección contra inyecciones SQL mediante SQLAlchemy
## 📚 Documentación Adicional

Accede a la documentación automática:
- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`


🗂️ Estructura de Carpetas
BackendServiNet/
│
├── config/              # Configuración general del sistema
├── crud/                # Operaciones de base de datos
├── models/              # Definición de modelos con SQLAlchemy
├── routes/              # Rutas de la API
├── schemas/             # Esquemas de validación con Pydantic
├── services/            # Servicios como autenticación, tokens, seguridad
│   ├── portador_token.py
│   └── seguridad.py
├── main.py              # Punto de entrada principal
├── README.md            # Documentación
├── requirements.txt     # Dependencias del proyecto


```
