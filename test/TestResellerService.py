import unittest

from run import create_app
from service.ResellerService import ResellerService
from util.CustomException import InvalidDataException, DuplicateDataException, NotFoundException


class ResellerServiceTest(unittest.TestCase):
    CONST_CPF = "CPF01"

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()
        self.reseller_service = ResellerService()

    def test_11_add(self):
        reseller = {"cpf": self.CONST_CPF, "email": "email@email.com", "password": "senha"}
        duplicate_reseller = {"cpf": self.CONST_CPF, "email": "email@email.com", "password": "senha"}
        invalid_reseller = {"cpf": self.CONST_CPF, "password": ""}
        new_reseller = self.reseller_service.add(reseller)
        assert new_reseller["cpf"] == self.CONST_CPF
        with self.assertRaises(InvalidDataException):
            self.reseller_service.add(invalid_reseller)
        with self.assertRaises(DuplicateDataException):
            self.reseller_service.add(duplicate_reseller)

    def test_12_find_by_cpf(self):
        data = self.reseller_service.find_by_cpf(cpf=self.CONST_CPF)
        with self.assertRaises(NotFoundException):
            self.reseller_service.find_by_cpf(cpf=-1)
        assert data["cpf"] == self.CONST_CPF

    def test_13_delete(self):
        data = self.reseller_service.find_by_cpf(cpf=self.CONST_CPF)
        delete = self.reseller_service.delete(id_reseller=data["id"])
        with self.assertRaises(NotFoundException):
            self.reseller_service.delete(id_reseller=-1)
        assert delete > 0


if __name__ == '__main__':
    unittest.main()
