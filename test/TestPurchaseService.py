import unittest

from run import create_app
from service.PurchaseService import PurchaseService
from service.ResellerService import ResellerService
from util.CustomException import NotFoundException, ConsumeApiException, InvalidDataException


class TestPurchaseService(unittest.TestCase):
    CONST_CPF = "153.509.460-56"

    # id = fields.Integer(required=False)
    # code = fields.Integer(required=True)
    # value = fields.Float(required=True)
    # date = fields.DateTime()
    # cpf = fields.String(required=True)
    # status = fields.String(required=False)

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()
        self.purchase_repository = PurchaseService()
        self.reseller_service = ResellerService()
        self.id_reseller = self.reseller_service.add(
            {"cpf": self.CONST_CPF, "email": "email@email.com", "password": "senha"})

    def tearDown(self):
        self.reseller_service.delete(self.id_reseller["id"])

    def test_01_add(self):
        purchase = {"cpf": self.CONST_CPF, "code": "A11", "value": 100.50, "date": "2019-01-01T22:50:00"}
        invalid_purchase = {"cpf": self.CONST_CPF, "code": "A11", "value": 12.50}
        data = self.purchase_repository.add(purchase=purchase)
        with self.assertRaises(InvalidDataException):
            self.purchase_repository.add(purchase=invalid_purchase)
        assert data["id"] > 0

    def test_02_update(self):
        purchase = self.purchase_repository.find_by_cpf(cpf=self.CONST_CPF)
        purchase[0]["value"] = 33.60
        data = self.purchase_repository.update(purchase=purchase[0])
        not_found_purchase = {"cpf": self.CONST_CPF, "code": "A11", "value": 20.50, "date": "2019-01-01T22:50:00",
                              "id": -2}
        with self.assertRaises(NotFoundException):
            self.purchase_repository.update(purchase=not_found_purchase)
        assert data["id"] > 0

    def test_03_find_by_cpf(self):
        data = self.purchase_repository.find_by_cpf(cpf=self.CONST_CPF)
        with self.assertRaises(NotFoundException):
            self.purchase_repository.find_by_cpf(cpf="CFP10")
        assert data[0]["id"] > 0

    def test_04_cash_back(self):
        data = self.purchase_repository.cash_back(cpf=self.CONST_CPF)
        with self.assertRaises(ConsumeApiException):
            self.purchase_repository.cash_back(cpf="CFP")
        assert data > 0

    def test_05_delete(self):
        purchase = self.purchase_repository.find_by_cpf(cpf=self.CONST_CPF)
        data = self.purchase_repository.delete(id_purchase=purchase[0]["id"])
        with self.assertRaises(NotFoundException):
            self.purchase_repository.delete(id_purchase="CFP10")
        assert data > 0