import decimal
import json

from flask import jsonify, make_response


def get_response(data, code):
    return make_response(jsonify({"body": data}), code)


def get_error_response(error, code):
    message = str(error.args)
    message = message.translate({ord('('): None})
    message = message.translate({ord(')'): None})
    message = message.translate({ord(','): None})
    response = make_response(jsonify(body=message), 400)
    return response


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)
