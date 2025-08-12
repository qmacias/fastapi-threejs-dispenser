import uvicorn

from typing import NamedTuple

from settings import settings


class DispenserConfig(NamedTuple):
    app: str = settings.DISPENSER_BACKEND_APP
    host: str = settings.DISPENSER_BACKEND_APP_HOST
    port: int = settings.DISPENSER_BACKEND_APP_PORT


def run_dispenser_backend() -> None:
    config = DispenserConfig()

    uvicorn.run(**config._asdict(), reload=True)
