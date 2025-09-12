import logging

from dishka import make_container, Container

from app.bootstrap.configs import Config, DatabaseConfig, AmoCRMConfig
from app.bootstrap.ioc.application import ApplicationProvider
from app.bootstrap.ioc.config import AppSetupProvider

logger = logging.getLogger(__name__)


def fastapi_container(
        config: Config,
) -> Container:
    logger.info("Fastapi DI setup")

    return make_container(
        AppSetupProvider(),
        ApplicationProvider(),
        context={
            DatabaseConfig: config.database,
            AmoCRMConfig: config.amocrm,
        },
    )
