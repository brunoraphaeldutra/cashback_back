from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, abort

from service.ResellerService import ResellerService
from util.ResponseUtil import get_response, get_error_response

service = ResellerService()


class ResellerResource(Resource):
    method_decorators = [jwt_required]

    def post(self):
        try:
            json_data = request.get_json(force=True)
            data = service.add(json_data)
            return get_response(data, 200)
        except Exception as err:
            response = get_error_response(err, 400)
            abort(response)

    def get(self):
        try:
            current_user = get_jwt_identity()
            data = service.find_by_cpf(current_user)

            return get_response(data, 200)
        except Exception as err:
            response = get_error_response(err, 400)
            abort(response)
