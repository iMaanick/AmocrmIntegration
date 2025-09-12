import logging

from dishka import make_container, Container

from app.bootstrap.configs import Config, RedisConfig, AmoCRMConfig
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
        },
    )
