import unittest
from datetime import datetime

from data.Model import Purchase
from data.Repository import ResellerRepository
from data.Repository import PurchaseRepository
from run import create_app
from util.CustomException import DuplicateDataException


class RepositoryTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()
        self.reseller_repository = ResellerRepository()
        self.purchase_repository = PurchaseRepository()

    def test_01_reseller_add(self):
        data = self.reseller_repository.add(cpf="CPF", email="email", password="password")
        assert data.cpf == "CPF"
        with self.assertRaises(DuplicateDataException):
            self.reseller_repository.add(cpf="CPF", email="email", password="password")

    def test_02_reseller_find_by_cpf(self):
        data = self.reseller_repository.find_by_cpf(cpf="CPF")
        assert data.cpf == "CPF"

    def test_03_reseller_login(self):
        data = self.reseller_repository.login(cpf="CPF", password="password")
        assert data.cpf == "CPF"

    def test_04_purchase_add(self):
        resseler = self.reseller_repository.find_by_cpf(cpf="CPF")
        print(resseler)
        purchase = Purchase(cpf="CPF", data=datetime.now()
                            , reseller_id=resseler.id
                            , codigo="A10", valor=25.30, status="A")
        data = self.purchase_repository.add(purchase)
        assert data.codigo == "A10"
        assert data.reseller.cpf == "CPF"

    def test_05_purchase_find_by_cpf(self):
        data = self.purchase_repository.find_by_cpf(cpf="CPF")
        assert data[0].cpf == "CPF"

    def test_06_purchase_update(self):
        datas = self.purchase_repository.find_by_cpf(cpf="CPF")
        purchase = datas[0]
        purchase.valor = 32.50
        data = self.purchase_repository.update(purchase)
        assert data.valor == 32.50

    def test_07_purchase_delete(self):
        data = self.purchase_repository.find_by_cpf(cpf="CPF")
        delete = self.purchase_repository.delete(id_purchase=data[0].id)
        assert delete > 0

    def test_08_reseller_delete(self):
        data = self.reseller_repository.find_by_cpf(cpf="CPF")
        delete = self.reseller_repository.delete(id_reseller=data.id)
        assert delete > 0


if __name__ == '__main__':
    unittest.main()