import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    
    DB_HOST = os.environ.get('DB_HOST') or 'Set-ip-Address'
    DB_USER = os.environ.get('DB_USER') or 'flaskuser'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'Aa123456'
    DB_NAME = os.environ.get('DB_NAME') or 'userregistration'