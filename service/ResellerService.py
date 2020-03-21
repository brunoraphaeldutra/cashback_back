import logging

from flask_restplus import ValidationError

from data.Repository import ResellerRepository
from service.FactoryService import ResellerToObject
from util.CustomException import InvalidDataException
from util.Validators import CreateResellerSchema

create_schema = CreateResellerSchema()
repository = ResellerRepository()


class ResellerService:

    def add(self, reseller):
        try:
            logging.info('Start create reseller')
            data = create_schema.load(reseller)
            object = ResellerToObject.get_reseller(reseller)
            return create_schema.dump(repository.add(object))
        except ValidationError as valid_error:
            raise InvalidDataException(valid_error)
        except Exception as err:
            raise Exception(err)

    def delete(self, reseller_id):
        try:
            logging.info('Start delete reseller')
            return create_schema.dump(repository.delete(reseller_id))
        except Exception as err:
            if type(err) is InvalidDataException:
                raise InvalidDataException(err)
            else:
                raise Exception(err)
