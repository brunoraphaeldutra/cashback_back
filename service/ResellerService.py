import logging

from marshmallow import ValidationError

from data.Repository import ResellerRepository
from service.FactoryService import ResellerToObject
from util.CustomException import InvalidDataException, DuplicateDataException, NotFoundException
from util.CustomException import NotMappedException
from util.StringUtil import StringUtil
from util.Validators import CreateResellerSchema


class ResellerService:
    create_schema = CreateResellerSchema()
    repository = ResellerRepository()

    def add(self, reseller):
        try:
            logging.info('Start create reseller')
            self.create_schema.load(reseller)
            data = ResellerToObject.get_reseller(reseller)
            return self.create_schema.dump(self.repository.add(data))
        except ValidationError as valid_error:
            raise InvalidDataException(valid_error)
        except DuplicateDataException as duplicate_error:
            raise DuplicateDataException(duplicate_error)
        except Exception as err:
            raise NotMappedException(err)

    def find_by_cpf(self, cpf: str):
        try:
            only_cpf = StringUtil.get_cpf(cpf)
            data = self.repository.find_by_cpf(cpf=only_cpf)
            return self.create_schema.dump(data)
        except NotFoundException:
            raise NotFoundException(message='Not found')
        except Exception as err:
            raise NotMappedException(message=err)

    def login(self, cpf: str, password: str):
        try:
            only_cpf = StringUtil.get_cpf(cpf)
            data = self.repository.login(cpf=only_cpf, password=password)
            return self.create_schema.dump(data)
        except NotFoundException:
            raise NotFoundException('Not found')
        except Exception as err:
            raise NotMappedException(err)

    def delete(self, id_reseller):
        try:
            logging.info('Start delete reseller')
            return self.repository.delete(id_reseller)
        except NotFoundException:
            raise NotFoundException('Not found')
        except InvalidDataException as err:
            raise InvalidDataException(err)
        except Exception as err:
            raise NotMappedException(err)
