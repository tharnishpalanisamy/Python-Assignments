# Common base for legacy imports; standard code uses ValueError
class UserNotFoundException(ValueError):
    pass

class InvalidEmailException(ValueError):
    pass

class UserNotAuthenticatedException(ValueError):
    pass

class LoanNotFoundException(ValueError):
    pass