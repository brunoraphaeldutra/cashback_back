from flask_marshmallow import Schema
from marshmallow import fields


class CreateResellerSchema(Schema):
    id = fields.Integer(required=False)
    cpf = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class DeleteResellerSchema(Schema):
    id = fields.Integer(required=True)
    cpf = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
