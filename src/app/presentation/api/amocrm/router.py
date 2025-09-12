import logging

from dishka import FromDishka
from dishka.integrations.fastapi import inject_sync
from fastapi import APIRouter

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
        "Upsert lead request received | row=%s email=%s amount=%s comment=%s",
        request_data.row,
        request_data.email,
        request_data.amount,
        request_data.comment,
    )
    response = use_case(request_data)
    logger.info(
        "Upsert lead processed successfully | id=%s",
        response.id,
    )
    return response
