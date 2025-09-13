from dataclasses import dataclass
from os import environ


class MissingRedisConfigError(ValueError):
    def __init__(self) -> None:
        super().__init__(self.title)

    @property
    def title(self) -> str:
        return "Required Redis environment variables are missing"


@dataclass(frozen=True)
class RedisConfig:
    host: str
    port: int
    username: str
    password: str


def load_redis_config() -> RedisConfig:
    host = environ.get("REDIS_HOST")
    port = environ.get("REDIS_PORT")
    username = environ.get("REDIS_USERNAME")
    password = environ.get("REDIS_PASSWORD")

    if (
            host is None
            or port is None
            or username is None
            or password is None
    ):
        raise MissingRedisConfigError

    return RedisConfig(
        host=host,
        port=int(port),
        username=username,
        password=password
    )


class MissingAmoCRMConfigError(ValueError):
    def __init__(self) -> None:
        super().__init__(self.title)

    @property
    def title(self) -> str:
        return "Required AmoCRM environment variables are missing"


@dataclass(frozen=True)
class AmoCRMConfig:
    access_token: str
    client_id: str
    client_secret: str
    subdomain: str
    redirect_url: str
    pipeline_id: str
    status_id: str


def load_amocrm_config() -> AmoCRMConfig:
    access_token = environ.get("AMOCRM_ACCESS_TOKEN")
    client_id = environ.get("AMOCRM_CLIENT_ID")
    client_secret = environ.get("AMOCRM_CLIENT_SECRET")
    subdomain = environ.get("AMOCRM_SUBDOMAIN")
    redirect_url = environ.get("AMOCRM_REDIRECT_URL")
    pipeline_id = environ.get("AMOCRM_PIPELINE_ID")
    status_id = environ.get("AMOCRM_STATUS_ID")

    if (
            access_token is None
            or client_id is None
            or client_secret is None
            or subdomain is None
            or redirect_url is None
            or pipeline_id is None
            or status_id is None
    ):
        raise MissingAmoCRMConfigError

    return AmoCRMConfig(
        access_token=access_token,
        client_id=client_id,
        client_secret=client_secret,
        subdomain=subdomain,
        redirect_url=redirect_url,
        pipeline_id=pipeline_id,
        status_id=status_id,
    )


@dataclass(frozen=True)
class Config:
    database: RedisConfig
    amocrm: AmoCRMConfig


def load_settings() -> Config:
    database = load_redis_config()
    amocrm = load_amocrm_config()
    return Config(
        database=database,
        amocrm=amocrm
    )
