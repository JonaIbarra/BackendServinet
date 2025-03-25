from fastapi import FastAPI
from routes.usuarios_direcciones_routes import usuario_direcciones_routes
from routes.persona_moral_routes import persona_moral_routes
from routes.persona_fisica_routes import persona_fisica_routes
from routes.persona_routes import persona_routes
from routes.usuario_routes import usuario_routes
from routes.direcciones_routes import direcciones_routes
from routes.rol_routes import rol_routes
from routes.usuario_rol_routes import usuario_rol_routes
from routes.servicios_routes import servicios_routes
from routes.citas_routes import citas_routes
from routes.sucursales_routes import sucursales_routes
from routes.horarios_routes import horarios_routes
from routes.ubicaciones_routes import ubicaciones_router
from routes.promociones_routes import promociones_routes
from routes.categorias_routes import categorias_routes
from routes.medio_contactos_routes import medio_contactos_router
from routes.cancelaciones_routes import cancelaciones_routes
from config.db import engine, Base
from fastapi import FastAPI

app = FastAPI(
    title="API Servinet",  # Título de la API
    version="1.0.0",
    description="Documentación de la API de Servinet"
)


@app.get("/")
async def root():
    return {"Hello": "World"}


    


app.include_router(persona_fisica_routes, tags=["Personas Fisicas"])
app.include_router(persona_routes, tags=["Personas"])
app.include_router(persona_moral_routes, tags=["Personas Morales"])
app.include_router(usuario_routes, tags=["Usuarios"])
app.include_router(direcciones_routes, tags=["Direcciones"])
app.include_router(rol_routes, tags=["Roles"])
app.include_router(usuario_rol_routes, tags=["Usuarios Roles"])
app.include_router(usuario_direcciones_routes, tags=["Usuarios Direcciones"])
app.include_router(servicios_routes, tags=["Servicios"])
app.include_router(citas_routes, tags=["Citas"])
app.include_router(sucursales_routes, tags=["Sucursales"])
app.include_router(horarios_routes, tags=["Horarios"])
app.include_router(ubicaciones_router, tags=["Ubicaciones"])
app.include_router(promociones_routes, tags=["Promociones"])
app.include_router(categorias_routes, tags=["Categorias"])
app.include_router(medio_contactos_router, tags=["Medio Contactos"])
app.include_router(cancelaciones_routes, tags=["Cancelaciones"])





# Crear todas las tablas
Base.metadata.create_all(bind=engine)