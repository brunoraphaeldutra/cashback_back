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
