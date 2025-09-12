import logging
from dataclasses import dataclass

from pydantic import EmailStr

from app.application.common.ports.lead_dto import LeadCreate
from app.application.common.ports.lead_gateway import LeadGateway

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class UpsertLeadRequest:
    row: int
    email: EmailStr
    amount: int
    comment: str


@dataclass(slots=True, frozen=True)
class UpsertLeadResponse:
    id: int


@dataclass(slots=True, frozen=True)
class UpsertLeadUseCase:
    lead_gateway: LeadGateway

    def __call__(self, request_data: UpsertLeadRequest) -> UpsertLeadResponse:
        lead_id = self.lead_gateway.create(
            LeadCreate(
                row=request_data.row,
                email=request_data.email,
                amount=request_data.amount,
                comment=request_data.comment,
            )
        )
        return UpsertLeadResponse(lead_id)
