from decimal import Decimal

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, validate
from sqlalchemy.orm import validates

ma = Marshmallow()
db = SQLAlchemy()


class Reseller(db.Model):
    __tablename__ = 'reseller'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(250), nullable=False, unique=True)
    full_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, cpf: str, email: str, password: str, full_name: str):
        self.full_name = full_name
        self.cpf = cpf
        self.email = email
        self.password = password

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return "<{}({!r})>".format(self.__class__.__name__, self.__dict__)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address


class Purchase(db.Model):
    __tablename__ = 'purchase'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(250), nullable=False)
    value = db.Column(db.Numeric, nullable=False)
    value_cb = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=True, default='')
    cpf = db.Column(db.String(20), nullable=False, default='')
    date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    reseller_id = db.Column(db.Integer, db.ForeignKey('reseller.id', ondelete='CASCADE'), nullable=False)
    reseller = db.relationship('Reseller', backref=db.backref('purchase', lazy='dynamic'))

    def __init__(self, code: str, value: Decimal, date: str, cpf: str, status: str, reseller_id: int):
        self.code = code
        self.value = value
        self.date = date
        self.cpf = cpf
        self.status = status
        self.reseller_id = reseller_id
        self.value_cb = 0

    def __str__(self):
        return self.cpf

    def __repr__(self):
        return "<{}({!r})>".format(self.__class__.__name__, self.__dict__)


class ResellerSchema(ma.Schema):
    id = fields.Integer(dump_only=False)
    full_name = fields.String(required=True)
    cpf = fields.String(required=True, validate=validate.Length(11))
    email = fields.String(required=True, validate=validate.Length(50))
    password = fields.String(required=True, validate=validate.Length(5))


class PurchaseSchema(ma.Schema):
    id = fields.Integer(dump_only=False)
    code = fields.Integer(required=True)
    value = fields.Number(required=True)
    date = fields.DateTime()
    cpf = fields.String(required=True, validate=validate.Length(11))
    status = fields.String(required=True)
