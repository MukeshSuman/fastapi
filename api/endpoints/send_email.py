from fastapi import APIRouter, BackgroundTasks
from mailer.mailer import send_email_async_test, send_email_background_test

router = APIRouter()


@router.get('/asynchronous')
async def send_email_asynchronous():
  await send_email_async_test()
  return 'Success'


@router.get('/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
  send_email_background_test(background_tasks)
  return 'Success'
