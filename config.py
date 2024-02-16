import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3b6a520a6f67388f4e02bdc1fa18c4c3'