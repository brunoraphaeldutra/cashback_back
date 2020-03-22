
from werkzeug.security import safe_str_cmp

from data.Repository import ResellerRepository

reseller_repository = ResellerRepository()


def authenticate(username, password):
    user = reseller_repository.login(cpf=username, password=password)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return reseller_repository.find_by_id(user_id)



