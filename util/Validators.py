from flask_marshmallow import Schema
from marshmallow import fields


class CreateResellerSchema(Schema):
    id = fields.Integer(required=False)
    cpf = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class CreatePurchaseSchema(Schema):
    id = fields.Integer(required=False)
    code = fields.String(required=True)
    value = fields.Float(required=True)
    value_cb = fields.Float(required=False)
    date = fields.DateTime(required=True)
    cpf = fields.String(required=True)
    status = fields.String(required=False)


class UpdatePurchaseSchema(Schema):
    id = fields.Integer(required=True)
    code = fields.String(required=True)
    value = fields.Float(required=True)
    value_cb = fields.Float(required=False)
    date = fields.DateTime()
    cpf = fields.String(required=True)
    status = fields.String(required=False)
