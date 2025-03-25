from datetime import timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import or_
from sqlalchemy.orm import Session
from config.db import SessionLocal
from crud import usuario_crud as crud
from models.usuario_model import Usuario
from schemas import usuario_schema as schemas
from services.auth import solicita_token, verify_password


usuario_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@usuario_routes.get("/usuarios", response_model=List[schemas.Usuario])
def obtener_todos_los_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_usuario = crud.obtener_todos_los_usuarios(db=db, skip=skip, limit=limit)
    return db_usuario

@usuario_routes.get("/usuarios/{id}", response_model=schemas.Usuario)
def obtener_usuario_por_ID(id: int, db: Session = Depends(get_db)):
    db_usuario = crud.obtener_usuario_por_ID(db=db, id=id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    return db_usuario


@usuario_routes.post("/usuarios", response_model=schemas.Usuario)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.obtener_usuario_por_nombre(db=db, nombre_usuario = usuario.nombre_usuario)
    if db_usuario:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return crud.crear_usuario(db=db, usuario=usuario)




@usuario_routes.put("/usuarios/{id}", response_model=schemas.Usuario)
def actualizar_usuario(id: int, usuario: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = crud.actualizar_usuario(db=db, id=id, usuario=usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    return db_usuario

@usuario_routes.delete("/usuarios/{id}", response_model=schemas.Usuario)
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    db_usuario = crud.eliminar_usuario(db=db, id=id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    return  db_usuario







@usuario_routes.post("/login/", response_model=schemas.UsuarioLogin, tags=["User Login"])
def read_credentials(usuario: schemas.UsuarioLogin, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(
        or_(
            Usuario.nombre_usuario == usuario.campo_login, 
            Usuario.correo_electronico == usuario.campo_login,
            Usuario.numero_telefono_movil == usuario.campo_login
        )
    ).first()
    
    if not db_usuario or not verify_password(usuario.contrasenia, db_usuario.contrasenia):
        return JSONResponse(content={'mensaje': 'Acceso denegado'}, status_code=404)

    token: str = solicita_token(usuario.dict())
    return JSONResponse(status_code=200, content=token)



