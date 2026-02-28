"""Error types for the Sportradar DataCore wrapper."""


class APIError(Exception):
    """Base class for all API wrapper errors."""


class AuthenticationError(APIError):
    """Authentication or token errors."""


class TransportError(APIError):
    """HTTP or network errors."""


class UnexpectedResponseError(APIError):
    """Unexpected or malformed API responses."""


class NotFoundError(APIError):
    """Requested entity not found."""


class ValidationError(APIError):
    """Invalid user input or parameters."""
