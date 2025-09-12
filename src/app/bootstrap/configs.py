from dataclasses import dataclass
from os import environ


@dataclass
class MissingDatabaseConfigError(ValueError):

    @property
    def title(self) -> str:
        return "Required db environment variables are missing"


@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    db_name: str
    user: str
    port: int
    password: str

    @property
    def uri(self) -> str:
        return (
            f"postgresql+psycopg://{self.user}:{self.password}@{self.host}"
            f":{self.port}/{self.db_name}"
        )


def load_database_config() -> DatabaseConfig:
    host = environ.get("DB_HOST")
    port = environ.get("POSTGRES_PORT")
    db_name = environ.get("POSTGRES_DB")
    user = environ.get("POSTGRES_USER")
    password = environ.get("POSTGRES_PASSWORD")

    if (
            host is None
            or port is None
            or db_name is None
            or user is None
            or password is None
    ):
        raise MissingDatabaseConfigError

    return DatabaseConfig(
        host=host,
        port=int(port),
        db_name=db_name,
        user=user,
        password=password,
    )

@dataclass
class MissingAmoCRMConfigError(ValueError):
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
    database: DatabaseConfig
    amocrm: AmoCRMConfig


def load_settings() -> Config:
    database = load_database_config()
    amocrm = load_amocrm_config()
    return Config(
        database=database,
        amocrm=amocrm
    )
