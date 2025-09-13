import logging
from urllib.parse import parse_qs

from dishka import FromDishka
from dishka.integrations.fastapi import inject_sync
from fastapi import APIRouter, Body
from starlette.responses import Response

from app.application.use_cases.lead_changed import LeadChangedUseCase
from app.application.use_cases.upsert_lead import (
    UpsertLeadRequest,
    UpsertLeadResponse,
    UpsertLeadUseCase,
)

logger = logging.getLogger(__name__)

amocrm_router = APIRouter()


@amocrm_router.post("/leads/upsert")
@inject_sync
def upsert_lead(
        request_data: UpsertLeadRequest,
        use_case: FromDishka[UpsertLeadUseCase],
) -> UpsertLeadResponse:
    logger.info(
        "Upsert lead request received | row=%s email=%s amount=%s",
        request_data.row,
        request_data.email,
        request_data.amount,
    )
    response = use_case(request_data)
    logger.info(
        "Upsert lead processed successfully | id=%s",
        response.id,
    )
    return response


@amocrm_router.post("/lead", response_class=Response)
@inject_sync
def lead_changed(
        use_case: FromDishka[LeadChangedUseCase],
        payload=Body(),
) -> None:
    decoded = payload.decode('utf-8', errors='replace')
    parsed = parse_qs(decoded)
    lead_id = int(parsed.get('leads[update][0][id]')[0])
    use_case(lead_id)
