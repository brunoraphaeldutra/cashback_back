import decimal
import json

from flask import jsonify, make_response


def get_response(data, code):
    return make_response(jsonify({"body": data, "code": code}, code))

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)