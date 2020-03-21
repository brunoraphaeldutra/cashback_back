import logging

from marshmallow import ValidationError

from data.Repository import ResellerRepository
from service.FactoryService import ResellerToObject
from util.CustomException import InvalidDataException, DuplicateDataException, NotFoundException
from util.CustomException import NotMappedException
from util.Validators import CreateResellerSchema


class ResellerService:
    create_schema = CreateResellerSchema()
    repository = ResellerRepository()

    def find_by_cpf(self, cpf: str):
        try:
            data = self.repository.find_by_cpf(cpf=cpf)
            return self.create_schema.dump(data)
        except NotFoundException as not_found_error:
            raise NotFoundException(not_found_error)
        except Exception as err:
            raise NotMappedException(err)

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

    def delete(self, id_reseller):
        try:
            logging.info('Start delete reseller')
            return self.create_schema.dump(self.repository.delete(id_reseller))
        except Exception as err:
            if type(err) is InvalidDataException:
                raise InvalidDataException(err)
            else:
                raise NotMappedException(err)
