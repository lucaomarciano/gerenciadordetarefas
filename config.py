import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '16052015Nar.'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:16052015Nar.@localhost:5432/task_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
