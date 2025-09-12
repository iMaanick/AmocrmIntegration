from dishka import Provider, Scope, provide_all, WithParents

from app.application.use_cases.upsert_lead import UpsertLeadUseCase
from app.infrastructure.adapters.lead_gateway import AMOLeadGateway


class ApplicationProvider(Provider):
    use_cases = provide_all(
        UpsertLeadUseCase,
        scope=Scope.REQUEST,
    )

    gateways = provide_all(
        WithParents[AMOLeadGateway],
        scope=Scope.REQUEST,
    )
