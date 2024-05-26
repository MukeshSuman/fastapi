from fastapi import APIRouter, status, Depends
import models
from pydantic import BaseModel
from mailer.mailer import send_email_contact_us
from typing import Annotated
from database import get_dbase
from sqlalchemy.orm import Session

router = APIRouter()


class ContactBase(BaseModel):
  first_name: str
  last_name: str
  company_name: str | None = None
  service: str
  email: str
  position: str
  message: str


db_dependecy = Annotated[Session, Depends(get_dbase)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def contact_us(contact_form: ContactBase, db: db_dependecy):
  db_contact_us = models.ContactUs(**contact_form.model_dump())
  db.add(db_contact_us)
  db.commit()
  email_contact_us_data = contact_form.model_dump()
  email_contact_us_data['name'] = email_contact_us_data[
      'first_name'] + ' ' + email_contact_us_data['last_name']
  await send_email_contact_us('Thank You for Contacting Us',
                              email_contact_us_data['email'],
                              email_contact_us_data)
  return {"message": "Thanks for contacting us!", "data": db_contact_us}


@router.get("/", status_code=status.HTTP_200_OK)
async def get_contact_us(db: db_dependecy):
  return db.query(models.ContactUs).filter_by(type='contact_us').all()
