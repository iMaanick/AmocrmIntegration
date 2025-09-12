from dataclasses import dataclass

from pydantic import EmailStr


@dataclass(slots=True)
class LeadCreate:
    row: int
    email: EmailStr
    amount: int
    comment: str
