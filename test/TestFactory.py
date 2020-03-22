import unittest

from run import create_app
from service.FactoryService import ResellerToObject


class ResellerToObjectTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()

    def test_21_get_reseller(self):
        reseller = {"cpf": "001-002-003-004-45", "email": "email@email.com", "password": "senha"}
        id_reseller = {"cpf": "001-002-003-004-45", "email": "email@email.com", "password": "senha", "id": 1}
        data = ResellerToObject.get_reseller(reseller)
        id_data = ResellerToObject.get_reseller(id_reseller)
        assert data.cpf == "00100200300445"
        assert id_data.id == 1
