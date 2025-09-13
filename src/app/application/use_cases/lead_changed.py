import logging
from dataclasses import dataclass

from app.application.common.ports.lead_gateway import LeadGateway
from app.application.common.ports.sheets_gateway import SheetsGateway
from app.application.common.ports.sheets_lead_gateway import SheetsLeadGateway

logger = logging.getLogger(__name__)


@dataclass(slots=True, frozen=True)
class LeadChangedUseCase:
    lead_gateway: LeadGateway
    sheets_lead_gateway: SheetsLeadGateway
    sheets_gateway: SheetsGateway

    def __call__(self, lead_id: int) -> None:
        lead = self.lead_gateway.get(lead_id)
        row_id = self.sheets_lead_gateway.get_row_by_lead(lead_id)
        if not row_id:
            return
        self.sheets_gateway.update_lead(row_id, lead.email, lead.amount)
