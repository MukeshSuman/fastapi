from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pathlib import Path
from config import EMAIL_HOST_SERVER, EMAIL_HOST_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from enum import Enum

EMAIL_TEMPLATE_FOLDER = Path('./templates/email')


class EmailTemplateName(Enum):
    CONTACT_US = 'contact.html'
    TEST_ASYNC = 'test_async.html'
    TEST_BACKGROUND = 'test_background.html'


class Envs:
    MAIL_USERNAME = EMAIL_HOST_USER
    MAIL_PASSWORD = EMAIL_HOST_PASSWORD
    MAIL_FROM = EMAIL_HOST_USER
    MAIL_PORT = EMAIL_HOST_PORT
    MAIL_SERVER = EMAIL_HOST_SERVER
    MAIL_FROM_NAME = 'Mithila IT'


print(Envs)

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
    await send_email_async(subject,
                           email_to,
                           data,
                           template_name=EmailTemplateName.CONTACT_US)


email_test_data = {'title': 'Mithila IT', 'name': 'Dev'}


async def send_email_async_test():
    email_test_data['title'] = email_test_data['title'] + ' ' + 'asynchronous'
    await send_email_async('MithilaIT Email Testing Asynchronous',
                           'sumanm686@gmail.com', email_test_data,
                           EmailTemplateName.TEST_ASYNC)


def send_email_background_test(background_tasks: BackgroundTasks):
    email_test_data['title'] = email_test_data['title'] + ' ' + 'Background'
    send_email_background(background_tasks,
                          'MithilaIT Email Testing Background',
                          'sumanm686@gmail.com', email_test_data,
                          EmailTemplateName.TEST_BACKGROUND)


async def send_email_async(subject: str, email_to: str, body: dict,
                           template_name: EmailTemplateName):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        bcc=[Envs.MAIL_FROM],
        template_body=body,
        subtype=MessageType.html,
    )

    print(conf)

    fm = FastMail(conf)
    await fm.send_message(message, template_name=template_name.value)


def send_email_background(background_tasks: BackgroundTasks, subject: str,
                          email_to: str, body: dict,
                          template_name: EmailTemplateName):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        bcc=[Envs.MAIL_FROM],
        template_body=body,
        subtype=MessageType.html,
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message,
                              message,
                              template_name=template_name.value)
