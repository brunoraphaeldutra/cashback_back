from flask_jwt_extended import create_access_token

from data.Repository import ResellerRepository
from util.CustomException import NotFoundException

reseller_repository = ResellerRepository()


def authenticate(username, password):
    try:
        reseller_repository.login(cpf=username, password=password)
        return create_access_token(identity=username)
    except NotFoundException:
        return None




