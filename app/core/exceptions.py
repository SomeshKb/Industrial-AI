class NotFoundError(Exception):
    """Raised when a requested resource cannot be found."""
    pass


class ValidationError(Exception):
    """Raised for input validation errors."""
    pass
