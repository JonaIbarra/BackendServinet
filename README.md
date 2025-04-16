# 📦 FastAPI - API de Gestión de Usuarios

Bienvenido a la API de Gestión de Usuarios desarrollada con **FastAPI**. Esta API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos de usuarios.

## 🚀 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) como servidor ASGI
- [SQLAlchemy](https://www.sqlalchemy.org/) para ORM
- [Pydantic](https://docs.pydantic.dev/) para validación de datos
- [SQLite](https://www.sqlite.org/index.html) como base de datos (puede reemplazarse fácilmente por PostgreSQL, MySQL, etc.)

---

## 📁 Estructura del proyecto

📦 fastapi-users-api ├── app │ ├── main.py │ ├── models.py │ ├── schemas.py │ ├── crud.py │ └── database.py ├── requirements.txt └── README.md

yaml
Copiar
Editar

---

## ⚙️ Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/fastapi-users-api.git
cd fastapi-users-api
2. Crea un entorno virtual (opcional pero recomendado)
bash
Copiar
Editar
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
3. Instala las dependencias
bash
Copiar
Editar
pip install -r requirements.txt
▶️ Ejecución del servidor
bash
Copiar
Editar
uvicorn app.main:app --reload
Esto levantará la API en: http://127.0.0.1:8000

📚 Documentación automática
FastAPI genera documentación automáticamente:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

📌 Endpoints principales

Método	Ruta	Descripción
GET	/users/	Listar todos los usuarios
GET	/users/{id}	Obtener usuario por ID
POST	/users/	Crear nuevo usuario
PUT	/users/{id}	Actualizar usuario existente
DELETE	/users/{id}	Eliminar usuario por ID
🧪 Pruebas (opcional)
Si tienes pruebas automatizadas, puedes indicarlo así:

bash
Copiar
Editar
pytest
📝 Notas adicionales
Esta API está pensada como base para proyectos más complejos.

Puedes integrar autenticación con JWT, OAuth2 o cualquier otro mecanismo.

📩 Contacto
Creado por Jonathan Enrique Ibarra Canales – ¡Con gusto puedes contribuir o dejar tus sugerencias!

🪪 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

yaml
Copiar
Editar

---

Si quieres que te lo genere como archivo `.md` listo para descarga, solo dime y te lo creo como archivo adjunto 📄👇.







