import logging

from dishka import Container, make_container

from app.bootstrap.configs import (
    AmoCRMConfig,
    Config,
    GoogleServiceAccountConfig,
    RedisConfig,
)
from app.bootstrap.ioc.application import ApplicationProvider
from app.bootstrap.ioc.config import AppSetupProvider
from app.bootstrap.ioc.infrastructure import InfrastructureProvider

logger = logging.getLogger(__name__)


def fastapi_container(
        config: Config,
) -> Container:
    logger.info("Fastapi DI setup")

    return make_container(
        AppSetupProvider(),
        ApplicationProvider(),
        InfrastructureProvider(),
        context={
            RedisConfig: config.database,
            AmoCRMConfig: config.amocrm,
            GoogleServiceAccountConfig: config.google_service_account,
        },
    )
