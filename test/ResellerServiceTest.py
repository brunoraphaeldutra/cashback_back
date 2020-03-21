import unittest

from run import create_app
from service.ResellerService import ResellerService
from util.CustomException import InvalidDataException, DuplicateDataException, NotFoundException


class ResellerTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()
        self.reseller_service = ResellerService()

    def test_01_add(self):
        reseller = {"cpf": "CPF", "email": "email@email.com", "password": "senha"}
        duplicate_reseller = {"cpf": "CPF", "email": "email@email.com", "password": "senha"}
        invalid_reseller = {"cpf": "CPF", "password": ""}
        new_reseller = self.reseller_service.add(reseller)
        assert new_reseller.cpf == "CPF"
        with self.assertRaises(InvalidDataException):
            self.reseller_service.add(invalid_reseller)
        with self.assertRaises(DuplicateDataException):
            self.reseller_service.add(duplicate_reseller)

    def test_02_find_by_cpf(self):
        data = self.reseller_service.find_by_cpf(cpf="CPF")
        with self.assertRaises(NotFoundException):
            self.reseller_service.find_by_cpf(id_purchase=-1)
        assert data["cpf"] == "CPF"

    def test_03_delete(self):
        data = self.reseller_service.find_by_cpf(cpf="CPF")
        delete = self.reseller_service.delete(id_reseller=data[0].id)
        with self.assertRaises(NotFoundException):
            self.reseller_service.delete(id_purchase=-1)
        assert delete > 0


if __name__ == '__main__':
    unittest.main()
