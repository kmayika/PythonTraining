class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

name = 'Kwezi'

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)
    elif len(name) > 20:
        raise NameTooLongError(name)



try:
    validate(name)
except BaseValidationError as err:
    err
    