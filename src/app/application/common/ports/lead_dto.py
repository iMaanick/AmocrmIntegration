from dataclasses import dataclass

from pydantic import EmailStr


@dataclass(slots=True)
class LeadCreate:
    row: int
    email: EmailStr
    amount: int

@dataclass(slots=True)
class LeadUpdate:
    email: EmailStr
    amount: int

@dataclass(slots=True)
class LeadFieldsData:
    email: str
    amount: int
