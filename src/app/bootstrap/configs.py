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
        password=password,
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


class MissingGoogleServiceAccountConfigError(ValueError):
    def __init__(self) -> None:
        super().__init__(self.title)

    @property
    def title(self) -> str:
        return "Required ServiceAccount environment variables are missing"


@dataclass(frozen=True)
class GoogleServiceAccountConfig:
    type: str
    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    auth_uri: str
    token_uri: str
    auth_provider_x509_cert_url: str
    client_x509_cert_url: str
    universe_domain: str
    spreadsheet_url: str
    spreadsheet_name: str


def load_google_service_account_config() -> GoogleServiceAccountConfig:
    type_ = environ.get("GOOGLE_TYPE")
    project_id = environ.get("GOOGLE_PROJECT_ID")
    private_key_id = environ.get("GOOGLE_PRIVATE_KEY_ID")
    private_key = environ.get("GOOGLE_PRIVATE_KEY")
    client_email = environ.get("GOOGLE_CLIENT_EMAIL")
    client_id = environ.get("GOOGLE_CLIENT_ID")
    auth_uri = environ.get("GOOGLE_AUTH_URI")
    token_uri = environ.get("GOOGLE_TOKEN_URI")
    auth_prov_x509_cert_url = environ.get("GOOGLE_AUTH_PROVIDER_X509_CERT_URL")
    client_x509_cert_url = environ.get("GOOGLE_CLIENT_X509_CERT_URL")
    universe_domain = environ.get("GOOGLE_UNIVERSE_DOMAIN")
    spreadsheet_url = environ.get("GOOGLE_SPREADSHEET_URL")
    spreadsheet_name = environ.get("GOOGLE_SPREADSHEET_NAME")

    if (
            type_ is None
            or project_id is None
            or private_key_id is None
            or private_key is None
            or client_email is None
            or client_id is None
            or auth_uri is None
            or token_uri is None
            or auth_prov_x509_cert_url is None
            or client_x509_cert_url is None
            or universe_domain is None
            or spreadsheet_url is None
            or spreadsheet_name is None
    ):
        raise MissingGoogleServiceAccountConfigError

    return GoogleServiceAccountConfig(
        type=type_,
        project_id=project_id,
        private_key_id=private_key_id,
        private_key=private_key,
        client_email=client_email,
        client_id=client_id,
        auth_uri=auth_uri,
        token_uri=token_uri,
        auth_provider_x509_cert_url=auth_prov_x509_cert_url,
        client_x509_cert_url=client_x509_cert_url,
        universe_domain=universe_domain,
        spreadsheet_url=spreadsheet_url,
        spreadsheet_name=spreadsheet_name,
    )


@dataclass(frozen=True)
class Config:
    database: RedisConfig
    amocrm: AmoCRMConfig
    google_service_account: GoogleServiceAccountConfig


def load_settings() -> Config:
    database = load_redis_config()
    amocrm = load_amocrm_config()
    google_service_account = load_google_service_account_config()
    return Config(
        database=database,
        amocrm=amocrm,
        google_service_account=google_service_account,
    )
