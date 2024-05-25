import os

EMAIL_HOST_SERVER = os.environ.get('EMAIL_HOST_SERVER')
EMAIL_HOST_PORT = int(os.environ.get('EMAIL_HOST_PORT') or '587')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
