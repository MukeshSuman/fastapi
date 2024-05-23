from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pathlib import Path
import json
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

EMAIL_TEMPLATE_FOLDER = Path('./templates/email')


class Envs:
    MAIL_USERNAME = EMAIL_HOST_USER
    MAIL_PASSWORD = EMAIL_HOST_PASSWORD
    MAIL_FROM = EMAIL_HOST_USER
    MAIL_PORT = EMAIL_PORT
    MAIL_SERVER = EMAIL_HOST
    MAIL_FROM_NAME = 'Mithila IT'


conf = ConnectionConfig(MAIL_USERNAME=Envs.MAIL_USERNAME,
                        MAIL_PASSWORD=Envs.MAIL_PASSWORD,
                        MAIL_FROM=Envs.MAIL_FROM,
                        MAIL_PORT=Envs.MAIL_PORT,
                        MAIL_SERVER=Envs.MAIL_SERVER,
                        MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
                        MAIL_STARTTLS=True,
                        MAIL_SSL_TLS=False,
                        USE_CREDENTIALS=True,
                        TEMPLATE_FOLDER=EMAIL_TEMPLATE_FOLDER)


async def send_email_contact_us(subject: str, email_to: str, data: dict):
    print('data', data)
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        bcc=[Envs.MAIL_FROM],
        template_body=data,
        subtype=MessageType.html,
    )

    fm = FastMail(conf)
    await fm.send_message(message, template_name='contact.html')


async def send_email_async(subject: str, email_to: str, body: dict):
    # body_str = json.dumps(body)
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        # body=html,
        template_body={
            'name': 'Mukesh Suman',
            'email': 'sumanm686@gmail.com',
            'company_name': '',
            'service': 'Service',
            'position': 'position',
            'comment': 'We need a static weebsite for our company',
        },
        subtype=MessageType.html,
    )

    fm = FastMail(conf)
    await fm.send_message(message, template_name='contact.html')


def send_email_background(background_tasks: BackgroundTasks, subject: str,
                          email_to: str, body: dict):
    body_str = json.dumps(body)
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body_str,
        subtype=MessageType.html,
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message,
                              message,
                              template_name='email.html')
