from flask_jwt_extended import create_access_token

from data.Repository import ResellerRepository

reseller_repository = ResellerRepository()


def authenticate(username, password):
    try:
        user = reseller_repository.login(cpf=username, password=password)
        return create_access_token(identity=username)
    except:
        return None




