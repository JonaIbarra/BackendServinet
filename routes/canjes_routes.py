from sqlalchemy.orm import Session
from config.db import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from crud import canjes_crud as crud
from schemas import canjes_schema as schemas



canjes_routes = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@canjes_routes.get("/canjes", response_model=schemas.Canjes)
def obtener_todos_los_canjes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_canjes = crud.obtener_todos_los_canjes(db=db, skip=skip, limit=limit)
    return db_canjes


@canjes_routes.get("/canjes/{id}", response_model=schemas.Canjes)
def obtener_canjes_por_ID(id: int, db: Session = Depends(get_db)):
    db_canjes = crud.obtener_canjes_por_ID(db=db, id=id)
    if db_canjes is None:
        raise HTTPException(status_code=404, detail="El canje no existe")
    return db_canjes

@canjes_routes.get("/canjes_por_cita/{cita_ID}", response_model=schemas.Canjes)
def obtener_canjes_por_cita(cita_ID: int, db: Session = Depends(get_db)):
    db_canjes = crud.obtener_canjes_por_cita(db=db, cita_ID=cita_ID)
    if db_canjes is None:
        raise HTTPException(status_code=404, detail="No se encontraron canjes para esta cita")
    return db_canjes

def obtener_canjes_por_usuario(usuario_ID: int, db: Session = Depends(get_db)):
    db_canjes = crud.obtener_canjes_por_usuario(db=db, usuario_ID=usuario_ID)
    if db_canjes is None:
        raise HTTPException(status_code=404, detail="No se encontraron canjes para este usuario")
    return db_canjes


@canjes_routes.post("/canjes", response_model=schemas.Canjes)
def crear_canjes(canjes: schemas.CanjesCreate, db: Session = Depends(get_db)):
    db_canjes = crud.validar_canje_existente(db=db, nombre=canjes.nombre, cita_ID=canjes.cita_ID)
    if db_canjes:
        raise HTTPException(status_code=400, detail="El canje ya existe")
    return crud.crear_canjes(db=db, canjes=canjes)

@canjes_routes.put("/canjes/{id}", response_model=schemas.Canjes)
def actualizar_canjes(id: int, canjes: schemas.CanjesUpdate, db: Session = Depends(get_db)):
    db_canjes = crud.actualizar_canjes(db=db, id=id, canjes=canjes)
    if db_canjes is None:
        raise HTTPException(status_code=404, detail="El canje no existe")
    return db_canjes

@canjes_routes.delete("/canjes/{id}", response_model=schemas.Canjes)
def eliminar_canjes(id: int, db: Session = Depends(get_db)):
    db_canjes = crud.eliminar_canjes(db=db, id=id)
    if db_canjes is None:
        raise HTTPException(status_code=404, detail="El canje no existe")
    return  db_canjes




