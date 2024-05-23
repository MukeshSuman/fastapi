# email_utils.py
import aiosmtplib
import asyncio
from email.message import EmailMessage
from typing import Optional

from config import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


async def send_email2(email_to: str, subject: str, body: str):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = email_to
    msg.set_content(body)

    smtp = aiosmtplib.SMTP(hostname=EMAIL_HOST, port=EMAIL_PORT)
    await smtp.connect()
    await smtp.starttls()
    await smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    await smtp.send_message(msg)
    await smtp.quit()


async def send_email(email_to: str,
                     subject: str,
                     body: str,
                     max_retries: int = 3,
                     retry_delay: int = 5):
    retries = 0
    while retries < max_retries:
        try:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = EMAIL_HOST_USER
            msg['To'] = email_to
            msg.set_content(body)

            smtp = aiosmtplib.SMTP(hostname=EMAIL_HOST, port=EMAIL_PORT)
            await smtp.connect()
            await smtp.starttls()
            await smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            await smtp.send_message(msg)
            await smtp.quit()
            return True
        except (aiosmtplib.SMTPException, asyncio.CancelledError,
                Exception) as e:
            retries += 1
            print(f"Error sending email (attempt {retries}): {e}")
            if retries == max_retries:
                print(f"Max retries ({max_retries}) reached. Email not sent.")
                return False
            await asyncio.sleep(retry_delay)

    return False
