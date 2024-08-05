import os

class Config:
    # Secret key for securing sessions (in a real app, use a proper secret key)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    
    # Database configuration
    # In production, these should be set as environment variables
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_USER = os.environ.get('DB_USER') or 'flaskuser'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'Aa123456'
    DB_NAME = os.environ.get('DB_NAME') or 'userregistration'