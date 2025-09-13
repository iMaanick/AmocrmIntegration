from dishka import Provider, Scope, WithParents, provide_all

from app.application.use_cases.lead_changed import LeadChangedUseCase
from app.application.use_cases.upsert_lead import UpsertLeadUseCase
from app.infrastructure.adapters.google_sheets import GoogleSheetsGateway
from app.infrastructure.adapters.lead_gateway import AMOLeadGateway
from app.infrastructure.adapters.redis_lead_google_sheets import (
    RedisSheetsLeadGateway,
)


class ApplicationProvider(Provider):
    use_cases = provide_all(
        UpsertLeadUseCase,
        LeadChangedUseCase,
        scope=Scope.REQUEST,
    )

    gateways = provide_all(
        WithParents[AMOLeadGateway],
        WithParents[RedisSheetsLeadGateway],
        scope=Scope.REQUEST,
    )
    sheets = provide_all(
        WithParents[GoogleSheetsGateway],
        scope=Scope.APP,
    )
