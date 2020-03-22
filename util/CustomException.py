class DuplicateDataException(Exception):
    pass


class NotFoundException(Exception):

    def __init__(self):
        super(Exception, self).__init__("Data not found")


class InvalidDataException(Exception):
    pass


class NotMappedException(Exception):
    pass


class ConsumeApiException(Exception):
    pass


class BusinessException(Exception):
    pass
