from flask import jsonify, make_response


def get_response(data, code):
    return make_response(jsonify({"body": data, "code": code}, code))