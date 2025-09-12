from dataclasses import dataclass

from app.application.common.exceptions.base import ApplicationError


@dataclass(slots=True, frozen=True)
class UnexpectedError(ApplicationError):
    pass
