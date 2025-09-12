from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from amocrm.v2.tokens import TokenManager
from dishka.integrations.fastapi import setup_dishka
from dotenv import load_dotenv
from fastapi import FastAPI

from app.bootstrap.configs import load_settings
from app.bootstrap.ioc.containers import fastapi_container
from app.bootstrap.logger import setup_logging
from app.presentation.api.root import root_router


def init_routers(app: FastAPI) -> None:
    app.include_router(root_router)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    app.state.dishka_container.get(TokenManager)
    yield
    app.state.dishka_container.close()

def create_app() -> FastAPI:
    load_dotenv()
    setup_logging()
    app = FastAPI(lifespan=lifespan)
    init_routers(app)
    config = load_settings()
    container = fastapi_container(config)
    setup_dishka(container=container, app=app)
    return app
