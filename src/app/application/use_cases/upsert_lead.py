import logging
from dataclasses import dataclass

from pydantic import EmailStr

from app.application.common.ports.lead_dto import LeadCreate, LeadUpdate
from app.application.common.ports.lead_gateway import LeadGateway
from app.application.common.ports.sheets_lead_gateway import SheetsLeadGateway

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class UpsertLeadRequest:
    row: int
    email: EmailStr
    amount: int


@dataclass(slots=True, frozen=True)
class UpsertLeadResponse:
    id: int


@dataclass(slots=True, frozen=True)
class UpsertLeadUseCase:
    lead_gateway: LeadGateway
    sheets_lead_gateway: SheetsLeadGateway

    def __call__(self, request_data: UpsertLeadRequest) -> UpsertLeadResponse:
        lead_id = self.sheets_lead_gateway.get_lead(request_data.row)
        if lead_id is not None:
            logger.info(
                "Lead exists for row %s: lead_id=%s",
                request_data.row,
                lead_id,
            )
            self.lead_gateway.update(
                lead_id=lead_id,
                data=LeadUpdate(
                    email=request_data.email,
                    amount=request_data.amount,
                ),

            )
            logger.info("Lead with lead_id=%s updated", lead_id)
            return UpsertLeadResponse(lead_id)
        else:
            logger.info("Lead does NOT exist for row %s", request_data.row)
            lead_id = self.lead_gateway.create(
                LeadCreate(
                    row=request_data.row,
                    email=request_data.email,
                    amount=request_data.amount,
                ),
            )
            logger.info("Lead with lead_id=%s created", lead_id)
            self.sheets_lead_gateway.set_lead(request_data.row, lead_id)
            return UpsertLeadResponse(lead_id)
