from marshmallow import Schema, fields


class CreateResellerSchema(Schema):
    id = fields.Int(required=False)
    cpf = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class UpdateResellerSchema(Schema):
    id = fields.Int(required=True)
    cpf = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
