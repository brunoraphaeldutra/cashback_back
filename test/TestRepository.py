import unittest
from datetime import datetime

from data.Model import Purchase, Reseller
from data.Repository import PurchaseRepository
from data.Repository import ResellerRepository
from run import create_app
from util.CustomException import DuplicateDataException, NotFoundException


class RepositoryTest(unittest.TestCase):
    CONST_CPF = "CPF"

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()
        self.reseller_repository = ResellerRepository()
        self.purchase_repository = PurchaseRepository()

    def test_01_reseller_add(self):
        reseller = Reseller(cpf=self.CONST_CPF, email="email@aa.com", password="password")
        duplicate_reseller = Reseller(cpf=self.CONST_CPF, email="email@aa.com", password="password")
        data = self.reseller_repository.add(reseller=reseller)
        assert data.cpf == self.CONST_CPF
        with self.assertRaises(DuplicateDataException):
            self.reseller_repository.add(reseller=duplicate_reseller)
        with self.assertRaises(AssertionError):
            Reseller(cpf="CPF1", email="email", password="password")

    def test_02_reseller_find_by_cpf(self):
        data = self.reseller_repository.find_by_cpf(cpf=self.CONST_CPF)
        with self.assertRaises(NotFoundException):
            self.reseller_repository.find_by_cpf(cpf="-1")
        assert data.cpf == self.CONST_CPF

    def test_03_reseller_login(self):
        data = self.reseller_repository.login(cpf=self.CONST_CPF, password="password")
        with self.assertRaises(NotFoundException):
            self.reseller_repository.login(cpf=self.CONST_CPF, password="passwords")
        assert data.cpf == self.CONST_CPF

    def test_04_purchase_add(self):
        reseller = self.reseller_repository.find_by_cpf(cpf=self.CONST_CPF)
        print(reseller)
        purchase = Purchase(cpf=self.CONST_CPF, date=datetime.now()
                            , reseller_id=reseller.id
                            , code="A10", value=25.30, status="A", value_cb=0)
        data = self.purchase_repository.add(purchase)
        assert data.code == "A10"
        assert data.reseller.cpf == self.CONST_CPF

    def test_05_purchase_find_by_cpf(self):
        data = self.purchase_repository.find_by_cpf(cpf=self.CONST_CPF)
        with self.assertRaises(NotFoundException):
            self.purchase_repository.find_by_cpf(cpf="-1")
        assert data[0].cpf == self.CONST_CPF

    def test_06_purchase_update(self):
        datas = self.purchase_repository.find_by_cpf(cpf=self.CONST_CPF)
        purchase = datas[0]
        purchase.value = 32.50
        data = self.purchase_repository.update(purchase)
        with self.assertRaises(NotFoundException):
            self.purchase_repository.find_by_cpf(cpf=-1)
        assert data.value == 32.50

    def test_07_purchase_delete(self):
        data = self.purchase_repository.find_by_cpf(cpf=self.CONST_CPF)
        delete = self.purchase_repository.delete(id_purchase=data[0].id)
        with self.assertRaises(NotFoundException):
            self.purchase_repository.delete(id_purchase=-1)
        assert delete > 0

    def test_08_reseller_delete(self):
        data = self.reseller_repository.find_by_cpf(cpf=self.CONST_CPF)
        delete = self.reseller_repository.delete(id_reseller=data.id)
        with self.assertRaises(NotFoundException):
            self.reseller_repository.delete(id_reseller=-1)
        assert delete > 0


if __name__ == '__main__':
    unittest.main()
