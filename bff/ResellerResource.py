from flask import request
from flask_restful import Resource

from service.ResellerService import ResellerService
from util.ResponseUtil import get_response

service = ResellerService()


class ResellerResource(Resource):

    def post(self):
        try:
            json_data = request.get_json(force=True)
            data = service.add(json_data)
            return get_response(data, 200)
        except Exception as err:
            return get_response(err.args, 500)


class LoginResource(Resource):

    def post(self):
        try:
            json_data = request.get_json(force=True)
            data = service.login(json_data["cpf"], json_data["password"])
            return get_response(data, 200)
        except Exception as err:
            return get_response(err.args, 500)
