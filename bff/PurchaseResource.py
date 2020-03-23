from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from service.PurchaseService import PurchaseService
from util.ResponseUtil import get_response

service = PurchaseService()


class PurchaseResource(Resource):
    method_decorators = [jwt_required]

    def post(self):
        try:
            json_data = request.get_json(force=True)
            data = service.add(json_data)
            return get_response(data, 200)
        except Exception as err:
            raise err

    def put(self):
        try:
            json_data = request.get_json(force=True)
            data = service.update(json_data)
            return get_response(data, 200)
        except Exception as err:
            return get_response(err.args, 500)

    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id_purchase', type=int, help='Value id for delete')
            args = parser.parse_args()
            data = service.delete(id_purchase=args["id_purchase"])
            return get_response(data, 200)
        except Exception as err:
            return get_response(err.args, 500)

    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('cpf', type=str, help='CPF for get purchases')
            args = parser.parse_args()
            data = service.find_by_cpf(cpf=args["cpf"])
            return get_response(data, 200)
        except Exception as err:
            return get_response(err.args, 500)


class CashBackResource(Resource):
    method_decorators = [jwt_required]

    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('cpf', type=str, help='CPF for get cash back value')
            args = parser.parse_args()
            data = service.cash_back(cpf=args["cpf"])
            return get_response(data, 200)
        except Exception as err:
            return get_response(err.args, 500)
