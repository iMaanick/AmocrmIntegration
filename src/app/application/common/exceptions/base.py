from dataclasses import dataclass
from typing import ClassVar


@dataclass(slots=True, frozen=True)
class ApplicationError(Exception):
    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        return "An application error occurred"
