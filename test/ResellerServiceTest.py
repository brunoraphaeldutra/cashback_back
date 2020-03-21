import unittest

from run import create_app
from service.ResellerService import ResellerService
from util.CustomException import InvalidDataException


class Reseller(unittest.TestCase):

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()
        self.reseller_service = ResellerService()

    def test_01_add(self):
        reseller = {"cpf": "CPF", "email": "email@email.com", "password": "senha"}
        invalid_reseller = {"cpf": "CPF", "password": ""}
        new_reseller = self.reseller_service.add(reseller)
        assert new_reseller.cpf == "CPF"
        with self.assertRaises(InvalidDataException):
            self.reseller_service.add(invalid_reseller)

    def test_02_delete(self):
        pass


if __name__ == '__main__':
    unittest.main()
