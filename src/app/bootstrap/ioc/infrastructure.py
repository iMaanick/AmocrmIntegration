import logging

from dishka import Provider, Scope, provide
from redis import Redis

from app.bootstrap.configs import RedisConfig

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
            decode_responses=True
        )
