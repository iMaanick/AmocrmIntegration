import logging

from dishka import Provider, Scope, provide
from google.oauth2.service_account import Credentials
from gspread import Client
from redis import Redis

from app.bootstrap.configs import RedisConfig
from app.infrastructure.adapters.google_sheets import GoogleCreds

logger = logging.getLogger(__name__)


class InfrastructureProvider(Provider):

    @provide(scope=Scope.APP)
    def get_client(
            self, config: RedisConfig,
    ) -> Redis:
        return Redis(
            host=config.host,
            port=config.port,
            username=config.username,
            password=config.password,
            decode_responses=True,
        )

    @provide(scope=Scope.APP)
    def get_sheets(
            self,
            creds_json: GoogleCreds,
    ) -> Client:
        creds = Credentials.from_service_account_info(creds_json)  # type: ignore[no-untyped-call]
        scoped = creds.with_scopes(
            [
                "https://www.googleapis.com/auth/spreadsheets",
            ],
        )
        return Client(scoped)
