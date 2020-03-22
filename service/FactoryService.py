from datetime import datetime

from data.Model import Reseller, Purchase


class ResellerToObject:

    @staticmethod
    def get_reseller(json):
        reseller = Reseller(cpf=json["cpf"],
                            email=json["email"], password=json["password"])
        if "id" in json:
            reseller.id = json["id"]
        return reseller


class PurchaseToObject:

    @staticmethod
    def get_purchase(json):
        python_date = datetime.strptime(json["date"], '%Y-%m-%dT%H:%M:%S')
        purchase = Purchase(code=json["code"],
                            value=json["value"], date=python_date,
                            cpf=json["cpf"], status=json["status"], reseller_id=json["reseller_id"])
        if "id" in json:
            purchase.id = json["id"]
        return purchase
