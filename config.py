from typing import List
from pydantic import BaseModel

EMAIL_HOST = 'smtp.hostinger.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@mithilait.com'
EMAIL_HOST_PASSWORD = '67yGyYrgMX#y04Er'


class MailBody(BaseModel):
  to: List[str]
  subject: str
  body: str
