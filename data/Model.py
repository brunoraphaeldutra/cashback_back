from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, validate

ma = Marshmallow()
db = SQLAlchemy()


class Reseller(db.Model):
    __tablename__ = 'reseller'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(250), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False)
    senha = db.Column(db.String(250), nullable=False)

    def __init__(self, cpf: str, email: str, senha: str):
        self.cpf = cpf
        self.email = email
        self.senha = senha


class Purchase(db.Model):

    __tablename__ = 'purchase'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(250), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=True, default='')
    cpf = db.Column(db.String(20), nullable=False, default='')
    data = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    reseller_id = db.Column(db.Integer, db.ForeignKey('reseller.id', ondelete='CASCADE'), nullable=False)
    reseller = db.relationship('Reseller', backref=db.backref('purchase', lazy='dynamic'))

    def __init__(self, codigo: str, valor: float, data: str, cpf: str, status: str, reseller_id: int):
        self.codigo = codigo
        self.valor = valor
        self.data = data
        self.cpf = cpf
        self.status = status
        self.reseller_id = reseller_id


class ResellerSchema(ma.Schema):
    id = fields.Integer(dump_only=False)
    cpf = fields.String(required=True, validate=validate.Length(11))
    email = fields.String(required=True, validate=validate.Length(50))
    senha = fields.String(required=True, validate=validate.Length(5))


class PurchaseSchema(ma.Schema):
    id = fields.Integer(dump_only=False)
    codigo = fields.Integer(required=True)
    valor = fields.Float(required=True)
    data = fields.DateTime()
    cpf = fields.String(required=True, validate=validate.Length(11))
    status = fields.String(required=True)