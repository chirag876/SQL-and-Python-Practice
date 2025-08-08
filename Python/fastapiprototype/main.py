from sqlalchemy.orm import Session
from . import models, database, crud, schemas
from fastapi import FastAPI, Depends

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/users", response_model=list[schemas.UserRead])
def getuser(db: Session = Depends(database.get_db)):
    return crud.get_user(db)

@app.post("/createusers", response_model=schemas.UserRead)
def createuser(user: schemas.UserCreate, db:Session=Depends(database.get_db)):
    return crud.create_user(db, user)