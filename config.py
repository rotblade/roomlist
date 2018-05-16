import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9c4240ee7db02716b3f1'
