from data.Model import Reseller


class ResellerToObject:

    @staticmethod
    def get_reseller(json):
        reseller = Reseller(cpf=json["cpf"],
                            email=json["email"], password=json["password"])
        if "id" in json:
            reseller.id = json["id"]
        return reseller