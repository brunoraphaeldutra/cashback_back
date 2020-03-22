from datetime import datetime

from data.Model import Reseller, Purchase
from util.StringUtil import StringUtil


class ResellerToObject:

    @staticmethod
    def get_reseller(json):
        only_cpf = StringUtil.get_cpf(json["cpf"])
        reseller = Reseller(cpf=only_cpf,
                            email=json["email"], password=json["password"])
        if "id" in json:
            reseller.id = json["id"]
        return reseller


class PurchaseToObject:

    @staticmethod
    def get_purchase(json):
        python_date = datetime.strptime(json["date"], '%Y-%m-%dT%H:%M:%S')
        only_cpf = StringUtil.get_cpf(json["cpf"])
        purchase = Purchase(code=json["code"],
                            value=json["value"], date=python_date,
                            cpf=only_cpf, status=json["status"], reseller_id=json["reseller_id"], value_cb=0)
        if "id" in json:
            purchase.id = json["id"]
        return purchase
