import unittest

from run import create_app
from service.FactoryService import ResellerToObject


class FactoryTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()

    def test_get_reseller(self):
        reseller = {"cpf": "CPF", "email": "email@email.com", "password": "senha"}
        id_reseller = {"cpf": "CPF", "email": "email@email.com", "password": "senha", "id": 1}
        data = ResellerToObject.get_reseller(reseller)
        id_data = ResellerToObject.get_reseller(id_reseller)
        assert data.cpf == "CPF"
        assert id_data.id == 1
