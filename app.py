from flask import Blueprint
from flask_restful import Api

from bff.PurchaseResource import PurchaseResource, CashBackResource
from bff.ResellerResource import ResellerResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(ResellerResource, '/reseller')
api.add_resource(PurchaseResource, '/purchase')
api.add_resource(CashBackResource, '/cashback')
