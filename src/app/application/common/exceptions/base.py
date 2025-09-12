from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ApplicationError(Exception):

    @property
    def title(self) -> str:
        return "An application error occurred"
