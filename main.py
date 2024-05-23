from fastapi import FastAPI, HTTPException, Depends, status, BackgroundTasks, Request
from pydantic import BaseModel
from typing import Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from email_utils import send_email
from send_email import send_email_background, send_email_async, send_email_contact_us
from config import MailBody
from mailer import send_mail
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="MithilaIT API Server")
models.Base.metadata.create_all(bind=engine)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    company_name: str | None = None
    servicetype: str
    email: str
    position: str
    message: str

class EmailContactDataBase (ContactBase):
    name: str | None = None
    pass


def get_dbase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependecy = Annotated[Session, Depends(get_dbase)]


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request,
                                      name="landing_page.html",
                                      context={
                                          "title": "MithilaIT API Server",
                                          "name": "Serve is Live"
                                      })


@app.post("/contact-us", status_code=status.HTTP_201_CREATED)
async def contact_us(contact_form: ContactBase, db: db_dependecy):
    db_contact_us = models.ContactUs(**contact_form.model_dump())
    db.add(db_contact_us)
    db.commit()
    email_contact_us_data = contact_form.model_dump()
    email_contact_us_data[
        'name'] = email_contact_us_data['first_name'] + ' ' + email_contact_us_data['last_name']
    email_contact_us_data['service'] = email_contact_us_data['servicetype']
    await send_email_contact_us('Thank You for Contacting Us',
                                email_contact_us_data['email'], email_contact_us_data)
    return {"message": "Thanks for contacting us!", "data": db_contact_us}


@app.get("/contact-us", status_code=status.HTTP_200_OK)
async def get_contact_us(db: db_dependecy):
    return db.query(models.ContactUs).all()


@app.post('/send-email')
async def send_email_endpoint(email_to: str, subject: str, body: str):
    await send_email(email_to, subject, body)
    return {'message': 'Email sent successfully'}


@app.get('/send-email/asynchronous')
async def send_email_asynchronous():
    await send_email_async('Contact Us', 'sumanm686@gmail.com', {
        'title': 'Hello World',
        'name': 'John Doe'
    })
    return 'Success'


@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks, 'Hello World',
                          'sumanm686@gmail.com', {
                              'title': 'Hello World',
                              'name': 'John Doe'
                          })
    return 'Success'


@app.post("/schedule-email")
def schedule_mail(req: MailBody, tasks: BackgroundTasks):
    data = req.model_dump()
    send_mail(data)
    # tasks.add_task(send_mail, data)
    return {"status": 200, "message": "email has been scheduled"}
