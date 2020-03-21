import logging

from data.Repository import ResellerRepository
from util.CustomException import InvalidDataException
from util.Validators import CreateResellerSchema

create_schema = CreateResellerSchema()
repository = ResellerRepository()


class ResellerService:

    def add(self, reseller):
        try:
            logging.info('Start create reseller')
            data, errors = CreateResellerSchema().load(reseller)
            if errors:
                raise InvalidDataException(errors)
            return create_schema.dump(repository.add(data))
        except Exception as err:
            raise InvalidDataException(err)
