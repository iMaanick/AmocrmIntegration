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
        logger.info("Checking changes for lead_id=%s", lead_id)

        lead = self.lead_gateway.get(lead_id)
        if lead is None:
            logger.warning("Lead with lead_id=%s not found", lead_id)
            return

        row_id = self.sheets_lead_gateway.get_row_by_lead(lead_id)
        if not row_id:
            logger.info("No row found in Sheets for lead_id=%s", lead_id)
            return

        logger.info(
            "Updating row=%s in Sheets with email=%s, amount=%s for lead_id=%s",
            row_id,
            lead.email,
            lead.amount,
            lead_id,
        )
        self.sheets_gateway.update_lead(row_id, lead.email, lead.amount)
        logger.info("Row=%s successfully updated for lead_id=%s", row_id, lead_id)