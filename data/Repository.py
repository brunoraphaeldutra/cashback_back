from sqlite3 import IntegrityError

from data.Model import db
from data.Model import ResellerSchema
from data.Model import Reseller
from data.Model import Purchase
from data.Model import PurchaseSchema
from util.CustomException import NotFoundException, DuplicateDataException


class ResellerRepository:
    reseller_schema = ResellerSchema()

    """ Find a reseller by a CPF.
    """

    def find_by_cpf(self, cpf: str):
        reseller = Reseller.query.filter_by(cpf=cpf).first()
        if reseller:
            return reseller
        else:
            raise NotFoundException

    """ Find a reseller by a CPF and password.
    """

    def login(self, cpf: str, password: str):
        reseller = Reseller.query.filter_by(cpf=cpf, password=password).first()
        if reseller:
            return reseller
        else:
            raise NotFoundException

    """ Add a reseller
    """

    def add(self, reseller: Reseller):
        try:
            # reseller = Reseller(cpf=cpf, email=email, senha=password)
            db.session.add(reseller)
            db.session.commit()
            return reseller
        except Exception:
            db.session.rollback()
            raise DuplicateDataException("Problem with insert")

    """ Delete a resseler
    """

    def delete(self, id_reseller: int):
        reseller = Reseller.query.filter_by(id=id_reseller).delete()
        if reseller:
            db.session.commit()
            return reseller
        else:
            raise NotFoundException("Data not found")

class PurchaseRepository:
    purchase_schema = PurchaseSchema()

    """ Find a purchase by a CPF of reseller.
    """

    def find_by_cpf(self, cpf: str):
        purchase = Purchase.query.filter_by(cpf=cpf)
        if purchase.first() is not None:
            return purchase
        else:
            raise NotFoundException

    """ Add a purchase
    """

    def add(self, purchase):
        try:
            db.session.add(purchase)
            db.session.commit()
            return purchase
        except Exception:
            raise DuplicateDataException("Problem with insert")

    """ Update a purchase
    """

    def update(self, purchase):
        db_purchase = Purchase.query.filter_by(id=purchase.id).first()
        if db_purchase:
            db_purchase.cpf = purchase.cpf
            db_purchase.status = purchase.status
            db_purchase.date = purchase.date
            db_purchase.value = purchase.value
            db_purchase.code = purchase.code
            db.session.commit()
            return db_purchase
        else:
            raise NotFoundException("Data not found")

    """ Delete a purchase
    """

    def delete(self, id_purchase: int):
        purchase = Purchase.query.filter_by(id=id_purchase).delete()
        if purchase:
            db.session.commit()
            return purchase
        else:
            raise NotFoundException("Data not found")