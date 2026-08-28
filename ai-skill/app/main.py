from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.routes.api import router as api_router
from app.core import errors
from app.core.config import get_app_settings
from app.core.events import lifespan
from app.services.exceptions import AuthException, ForbiddenException


def get_application() -> FastAPI:
    settings = get_app_settings()
    application = FastAPI(
        title=settings.project_name,
        version=settings.version,
        debug=settings.debug,
        lifespan=lifespan,
    )

    application.include_router(api_router)

    application.add_exception_handler(ValueError, errors.value_error_handler)
    application.add_exception_handler(
        ForbiddenException, errors.forbidden_error_handler
    )
    application.add_exception_handler(AuthException, errors.auth_error_handler)
    application.add_exception_handler(
        RequestValidationError, errors.http400_error_handler
    )
    application.add_exception_handler(Exception, errors.exception_handler)

    return application


app = get_application()
