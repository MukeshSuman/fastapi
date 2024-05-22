from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI(title="MithilaIT API Server")
models.Base.metadata.create_all(bind=engine)


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    company_name: str | None = None
    servicetype: str
    email: str
    postion: str
    message: str


def get_dbase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependecy = Annotated[Session, Depends(get_dbase)]


@app.get("/")
async def root():
    return {"message": "API is running"}


@app.post("/contact-us", status_code=status.HTTP_201_CREATED)
async def contact_us(contact_form: ContactBase, db: db_dependecy):
    db_contact_us = models.ContactUs(**contact_form.model_dump())
    db.add(db_contact_us)
    db.commit()
    return {"message": "Thanks for contacting us!", "data": db_contact_us}


@app.get("/contact-us", status_code=status.HTTP_200_OK)
async def get_contact_us(db: db_dependecy):
    return db.query(models.ContactUs).all()
