# from config import HOST, USERNAME, PASSWORD, PORT, MailBody
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, MailBody
from ssl import create_default_context
from email.mime.text import MIMEText
from smtplib import SMTP


def send_mail(data: dict | None = None):
    print('send_mail', data)
    msg = MailBody(subject='Test Email',
                   to=['sumanm686@gmail.com'],
                   body='This is a test email')
    message = MIMEText(msg.body, "html")
    message["From"] = EMAIL_HOST_USER
    message["To"] = ",".join(msg.to)
    message["Subject"] = msg.subject

    ctx = create_default_context()

    try:
        with SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.ehlo()
            server.starttls(context=ctx)
            server.ehlo()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.send_message(message)
            server.quit()
            print('ssss')
        return {"status": 200, "errors": None}
    except Exception as e:
        print(e)
        return {"status": 500, "errors": e}
