class ValidationError(Exception):
    pass


class InputValidationError(ValidationError):
    pass


class OutputValidationError(ValidationError):
    pass
