from fastapi import HTTPException, Request, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from services.auth import valida_token
import crud.usuario_crud, config.db



def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Portador(HTTPBearer):
    async def _call_(self, request: Request, db: Session = Depends(get_db)):
        autorizacion = await super()._call_(request)
        dato = valida_token(autorizacion.credentials)
        db_userlogin = crud.usuario_crud.get_user_by_creentials(db, username=dato["Nombre_Usuario"], password=dato["Contrasenia"])
        if db_userlogin is None:
            raise HTTPException(status_code=404, detail="LogIn incorrecto")
        return db_userlogin