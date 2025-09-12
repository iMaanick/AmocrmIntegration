from amocrm.v2 import tokens
from amocrm.v2.tokens import TokenManager
from dishka import Provider, Scope, provide, from_context

from app.bootstrap.configs import AmoCRMConfig
from app.infrastructure.adapters.lead_gateway import PipelineID, StatusId


class AppSetupProvider(Provider):
    scope = Scope.APP

    database_config = from_context(AmoCRMConfig)

    @provide
    def setup_amo(self, config: AmoCRMConfig) -> TokenManager:
        storage = tokens.MemoryTokensStorage()
        storage.save_tokens(
            access_token=config.access_token,
            refresh_token="",
        )
        return tokens.default_token_manager(
            client_id=config.client_id,
            client_secret=config.client_secret,
            subdomain=config.subdomain,
            redirect_url=config.redirect_url,
            storage=storage,
        )

    @provide
    def setup_pipeline_id(self, config: AmoCRMConfig) -> PipelineID:
        return PipelineID(int(config.pipeline_id))

    @provide
    def setup_status_id(self, config: AmoCRMConfig) -> StatusId:
        return StatusId(int(config.status_id))
