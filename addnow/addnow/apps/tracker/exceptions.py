class IncorrectEventException(Exception):
    pass


class TrimAPIException(Exception):
    pass


class BadTrimKeyException(TrimAPIException):
    pass


class ValidationFailedException(TrimAPIException):
    pass
