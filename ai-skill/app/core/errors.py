from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.logger import Logger
from app.services.exceptions import AuthException, ForbiddenException

logger = Logger(__file__)


async def value_error_handler(_: Request, exc: ValueError) -> JSONResponse:
    logger.error(str(exc))
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"errors": str(exc)},
    )


async def forbidden_error_handler(_: Request, exc: ForbiddenException) -> JSONResponse:
    logger.error(str(exc))
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={"errors": str(exc)},
    )


async def auth_error_handler(_: Request, exc: AuthException) -> JSONResponse:
    logger.error(str(exc))
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"errors": str(exc)},
    )


async def http400_error_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"errors": jsonable_encoder(exc.errors())},
    )


async def exception_handler(_: Request, exc: Exception) -> JSONResponse:
    logger.error(str(exc))
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"errors": str(exc)},
    )
