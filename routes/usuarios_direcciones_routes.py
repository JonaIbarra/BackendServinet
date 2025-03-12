from logging import config
from typing import List
from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
import config.db
from crud import usuarios_direcciones_crud as crud
import schemas.usuarios_direcciones_schema as schemas



usuario_direcciones_routes = APIRouter()


def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@usuario_direcciones_routes.get("/usuarios_models", response_model=List[schemas.UsuariosDirecciones])
def obtener_todos_los_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_usuario_direcciones = crud.obtener_todos_los_usuarios_direcciones(db=db, skip=skip, limit=limit)
    return db_usuario_direcciones


@usuario_direcciones_routes.get("/usuarios_models/{id}", response_model=schemas.UsuariosDirecciones)
def obtener_usuarios_por_ID(id: int, db: Session = Depends(get_db)):
    db_usuario_direcciones = crud.obtener_usuarios_direcciones_por_ID(db=db, id=id)
    if db_usuario_direcciones is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    return db_usuario_direcciones


@usuario_direcciones_routes.post("/usuarios_models", response_model=schemas.UsuariosDirecciones)
def crear_usuarios_direcciones(usuarios_direcciones: schemas.UsuariosDireccionesCreate, db: Session = Depends(get_db)):
    db_usuarios_direcciones = crud.crear_usuarios_direcciones(db=db, usuarios_direcciones=usuarios_direcciones)
    return db_usuarios_direcciones


@usuario_direcciones_routes.put("/usuarios_models/{id}", response_model=schemas.UsuariosDirecciones)
def actualizar_usuarios_direcciones(id: int, usuarios_direcciones: schemas.UsuariosDireccionesUpdate, db: Session = Depends(get_db)):
    db_usuarios_direcciones = crud.actualizar_usuarios_direcciones(db=db, id=id, usuarios_direcciones=usuarios_direcciones)
    if db_usuarios_direcciones is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    return db_usuarios_direcciones

@usuario_direcciones_routes.delete("/usuarios_models/{id}", response_model=schemas.UsuariosDirecciones) 
def eliminar_usuarios_direcciones(id: int, db: Session = Depends(get_db)):
    db_usuarios_direcciones = crud.eliminar_usuarios_direcciones(db=db, id=id)
    if db_usuarios_direcciones is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    return db_usuarios_direcciones

