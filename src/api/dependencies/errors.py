from typing import Any

from pydantic import BaseModel


class ErrorModel(BaseModel):
    errors: str | list[Any]


VALIDATE_ERROR_RESPONSE: dict[str, Any] = {
    "model": ErrorModel,
    "description": "Validation error",
}

NOT_FOUND_ERROR_RESPONSE: dict[str, Any] = {
    "model": ErrorModel,
    "description": "Resource not found",
}

FORBIDDEN_ERROR_RESPONSE: dict[str, Any] = {
    "model": ErrorModel,
    "description": "Forbidden",
}

AUTH_ERROR_RESPONSE: dict[str, Any] = {
    "model": ErrorModel,
    "description": "Unauthorized",
}
