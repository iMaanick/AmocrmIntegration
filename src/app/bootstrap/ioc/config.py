from amocrm.v2 import tokens
from amocrm.v2.tokens import TokenManager
from dishka import Provider, Scope, provide, from_context

from app.bootstrap.configs import AmoCRMConfig, RedisConfig, GoogleServiceAccountConfig
from app.infrastructure.adapters.google_sheets import GoogleCreds, SpreadsheetUrl, SpreadsheetName
from app.infrastructure.adapters.lead_gateway import PipelineID, StatusId


class AppSetupProvider(Provider):
    scope = Scope.APP

    database_config = from_context(RedisConfig)
    amo_config = from_context(AmoCRMConfig)
    google_service_account_config = from_context(GoogleServiceAccountConfig)

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

    @provide
    def google_config_to_creds_json(self, config: GoogleServiceAccountConfig) -> GoogleCreds:
        return GoogleCreds({
            "type": config.type,
            "project_id": config.project_id,
            "private_key_id": config.private_key_id,
            "private_key": config.private_key,
            "client_email": config.client_email,
            "client_id": config.client_id,
            "auth_uri": config.auth_uri,
            "token_uri": config.token_uri,
            "auth_provider_x509_cert_url": config.auth_provider_x509_cert_url,
            "client_x509_cert_url": config.client_x509_cert_url,
            "universe_domain": config.universe_domain,
        })

    @provide
    def setup_spreadsheet_url(self, config: GoogleServiceAccountConfig) -> SpreadsheetUrl:
        return SpreadsheetUrl(config.spreadsheet_url)

    @provide
    def setup_spreadsheet_name(self, config: GoogleServiceAccountConfig) -> SpreadsheetName:
        return SpreadsheetName(config.spreadsheet_name)