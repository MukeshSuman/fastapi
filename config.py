import os

EMAIL_HOST_SERVER = os.environ['EMAIL_HOST_SERVER'] or 'smtp.gmail.com'
EMAIL_HOST_PORT = int(os.environ['EMAIL_HOST_PORT'] or '587')
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER'] or 'fake@email.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] or 'fakepassword'

DB_SERVICE = 'mysql+mysqlconnector'
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
