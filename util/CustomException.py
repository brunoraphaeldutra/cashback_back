from werkzeug.exceptions import HTTPException

CONST_REP = '<{}: {}>\n'


class DuplicateDataException(Exception):

    def __init__(self, message: str):
        super(Exception, self).__init__(message)
        self.message = message

    def __str__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)


class NotFoundException(Exception):

    def __init__(self, message: str):
        super(Exception, self).__init__(message)
        self.message = message

    def __str__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)


class InvalidDataException(Exception):

    def __init__(self, message: str):
        super(Exception, self).__init__(message)
        self.message = message

    def __str__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)


class NotMappedException(Exception):

    def __init__(self, message: str):
        super(Exception, self).__init__(message)
        self.message = message

    def __str__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)


class ConsumeApiException(Exception):

    def __init__(self, message: str):
        super(Exception, self).__init__(message)
        self.message = message

    def __str__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)


class BusinessException(Exception):

    def __init__(self, message: str):
        super(Exception, self).__init__(message)
        self.message = message

    def __str__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)


class APIException(HTTPException):

    def __init__(self, message: str):
        super(Exception, self).__init__(message)
        self.message = message

    def __str__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)

    def __repr__(self):
        return CONST_REP.format(self.__class__.__name__, self.message)
