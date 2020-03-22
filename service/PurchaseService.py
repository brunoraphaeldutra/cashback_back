import logging

import requests
from marshmallow import ValidationError

from config import CPF_ADM, URL_CASH_BACK, TOKEN_CASH_BACK
from data.Repository import PurchaseRepository
from service.FactoryService import PurchaseToObject
from service.ResellerService import ResellerService
from util.CustomException import InvalidDataException, NotMappedException, NotFoundException, ConsumeApiException
from util.StringUtil import StringUtil
from util.Validators import CreatePurchaseSchema, UpdatePurchaseSchema


def _get_status(cpf):
    if StringUtil.get_cpf(cpf) == StringUtil.get_cpf(CPF_ADM):
        return 'Aprovado'
    else:
        return 'Em validação'


def _get_cash_back(value):
    if value <= 999:
        return 10
    elif 1000 <= value <= 1500:
        return 15
    else:
        return 20


class PurchaseService:
    create_schema = CreatePurchaseSchema()
    update_schema = UpdatePurchaseSchema()
    repository = PurchaseRepository()
    reseller_service = ResellerService()

    def add(self, purchase):
        try:
            logging.info('Start create purchase')
            self.create_schema.load(purchase)
            purchase["status"] = _get_status(purchase["cpf"])
            logging.info('Find a reseller by cpf purchase')
            reseller = self.reseller_service.find_by_cpf(purchase["cpf"])
            purchase["reseller_id"] = reseller["id"]
            data = PurchaseToObject.get_purchase(purchase)
            data.value_cb = _get_cash_back(data.value)
            return self.create_schema.dump(self.repository.add(data))
        except ValidationError as valid_error:
            raise InvalidDataException(valid_error)
        except Exception as err:
            raise NotMappedException(err)

    def update(self, purchase):
        try:
            logging.info('Start update purchase')
            self.update_schema.load(purchase)
            purchase["status"] = _get_status(purchase["cpf"])
            logging.info('Find a reseller by cpf purchase')
            reseller = self.reseller_service.find_by_cpf(purchase["cpf"])
            purchase["reseller_id"] = reseller["id"]
            data = PurchaseToObject.get_purchase(purchase)
            data.value_cb = _get_cash_back(data.value)
            return self.update_schema.dump(self.repository.update(data))
        except ValidationError as valid_error:
            raise InvalidDataException(valid_error)
        except NotFoundException:
            raise NotFoundException
        except Exception as err:
            raise NotMappedException(err)

    def delete(self, id_purchase):
        try:
            logging.info('Start delete purchase')
            return self.repository.delete(id_purchase)
        except NotFoundException:
            raise NotFoundException
        except Exception as err:
            raise NotMappedException(err)

    def find_by_cpf(self, cpf):
        try:
            logging.info('Start find purchase')
            only_cpf = StringUtil.get_cpf(cpf)
            return UpdatePurchaseSchema(many=True).dump(self.repository.find_by_cpf(only_cpf))
        except NotFoundException:
            raise NotFoundException
        except Exception as err:
            raise NotMappedException(err)

    def cash_back(self, cpf):
        try:
            only_cpf = StringUtil.get_cpf(cpf)
            if only_cpf == '':
                raise ConsumeApiException
            url = URL_CASH_BACK.format(only_cpf)
            header = {'token': TOKEN_CASH_BACK}
            response = requests.get(url, headers=header)
            return response.json()["body"]["credit"]
        except ConsumeApiException:
            raise ConsumeApiException
        except Exception as err:
            raise NotMappedException(err)
