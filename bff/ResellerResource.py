from flask_restful import Resource

from service.ResellerService import ResellerService

service = ResellerService()


class ResellerResource(Resource):

    def get(self):
        reseller = {"cpf": ""}
        service.add(reseller)
        return {"return": "it's run"}
