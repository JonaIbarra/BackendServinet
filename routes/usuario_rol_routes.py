from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import SessionLocal
from crud import usuario_rol_crud as crud
from schemas import usuario_rol_schema as schemas


usuario_rol_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@usuario_rol_routes.get("/usuarios_roles", response_model=List[schemas.UsuarioRol])
def obtener_todos_los_usuarios_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_usuario_rol = crud.obtener_todos_los_usuarios_roles(db=db, skip=skip, limit=limit)
    return db_usuario_rol


@usuario_rol_routes.get("/usuarios_roles/rol/{id}", response_model=schemas.UsuarioRol)
def obtener_usuario_rol_por_rol_ID(id: int, db: Session = Depends(get_db)):
    db_usuario_rol = crud.obtener_usuario_rol_por_rol_ID(db=db, id=id)
    if db_usuario_rol is None:
        raise HTTPException(status_code=404, detail="El usuario_rol no existe")
    return db_usuario_rol

@usuario_rol_routes.get("/usuarios_roles/usuario/{id}", response_model=schemas.UsuarioRol)
def obtener_usuario_rol_por_usuario_ID(id: int, db: Session = Depends(get_db)):
    db_usuario_rol = crud.obtener_usuario_rol_por_usuario_ID(db=db, id=id)
    if db_usuario_rol is None:
        raise HTTPException(status_code=404, detail="El usuario_rol no existe")
    return db_usuario_rol


@usuario_rol_routes.post("/usuarios_roles", response_model=schemas.UsuarioRol)
def crear_usuario_rol(usuario_rol: schemas.UsuarioRol, db: Session = Depends(get_db)):
    db_usuario_rol = crud.obtener_usuario_rol_por_rol_ID(db=db, id=usuario_rol.rol_ID)
    if db_usuario_rol:
        raise HTTPException(status_code=400, detail="El usuario_rol ya existe")
    return crud.crear_usuario_rol(db=db, usuario_rol=usuario_rol)

@usuario_rol_routes.put("/usuarios_roles/{id}", response_model=schemas.UsuarioRol)
def actualizar_usuario_rol(id: int, usuario_rol: schemas.UsuarioRolCreate, db: Session = Depends(get_db)):
    db_usuario_rol = crud.obtener_usuario_rol_por_usuario_ID(db=db, id=id)
    if db_usuario_rol is None:
        raise HTTPException(status_code=404, detail="El usuario_rol no existe")
    return crud.actualizar_usuario_rol(db=db, usuario_rol=usuario_rol)


