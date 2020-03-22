import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

CREATE_FIRST_RESELLER = True
LOG_NAME = "cashback_log.log"
CPF_ADM = "15350946056"
DEFAULT_PASSWORD = "senha"
URL_CASH_BACK = "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf={}"
TOKEN_CASH_BACK = "ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm"
