from werkzeug.exceptions import HTTPException


class DuplicateDataException(Exception):
    def __str__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)


class NotFoundException(Exception):

    def __init__(self):
        super(Exception, self).__init__("Data not found")

    def __str__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)


class InvalidDataException(Exception):

    def __init__(self, message: str):
        super(Exception, self).__init__(message)
        self.message = message

    def __str__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)


class NotMappedException(Exception):
    def __str__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)


class ConsumeApiException(Exception):
    def __str__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)


class BusinessException(Exception):
    def __str__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)


class APIException(HTTPException):

    def __str__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return '<{}: {}>\n'.format(self.__class__.__name__, self.message)


custom_errors = {
    'APIException': {
        'message': "A user with that username already exists.",
        'status': 409,
    }
}