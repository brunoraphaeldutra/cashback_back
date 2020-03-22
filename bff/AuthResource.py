from flask import request
from flask_restful import Resource

from service.JWTService import authenticate
from util.ResponseUtil import get_response


class AuthResource(Resource):

    def post(self):
        try:
            json_data = request.get_json(force=True)
            data = authenticate(json_data["username"], json_data["password"])
            if data:
                return get_response(data, 200)
            else:
                return get_response("Invalid usernamet/password", 401)
        except Exception as err:
            return get_response(err.args, 500)
