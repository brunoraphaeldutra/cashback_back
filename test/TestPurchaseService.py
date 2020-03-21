import unittest

from run import create_app
from service.PurchaseService import PurchaseService
from util.CustomException import NotFoundException


class TestPurchaseService(unittest.TestCase):
    CONST_CPF = "CPF_PURCHASE"

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()
        self.purchase_repository = PurchaseService()

    def test_01_add(self):
        purchase = {"cpf": self.CONST_CPF, "email": "email@email.com", "password": "senha"}
        invalid_purchase = {"cpf": self.CONST_CPF, "email": "email@email.com", "password": "senha"}
        data = self.purchase_repository.add(purchase=purchase)
        with self.assertRaises(AssertionError):
            self.purchase_repository.add(purchase=invalid_purchase)
        assert data["id"] > 0

    def test_02_update(self):
        purchase = {"cpf": self.CONST_CPF, "email": "email@email.com", "password": "senha"}
        not_found_purchase = {"cpf": self.CONST_CPF, "email": "email@email.com", "password": "senha"}
        data = self.purchase_repository.update(purchase=purchase)
        with self.assertRaises(NotFoundException):
            self.purchase_repository.add(purchase=not_found_purchase)
        assert data["id"] == 0

    def test_03_delete(self):
        purchase = self.purchase_repository.find_by_cpf(cpf=self.CONST_CPF)
        data = self.purchase_repository.delete(purchase["id"])
        with self.assertRaises(NotFoundException):
            self.purchase_repository.delete(cpf="CFP10")
        assert data > 0

    def test_03_find_by_cpf(self):
        data = self.purchase_repository.find_by_cpf(cpf=self.CONST_CPF)
        with self.assertRaises(NotFoundException):
            self.purchase_repository.find_by_cpf(cpf="CFP10")
        assert data[id] > 0

    def test_04_cash_back(self, cpf):
        pass