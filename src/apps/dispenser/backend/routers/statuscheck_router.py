from typing import Dict
from datetime import datetime

from fastapi import APIRouter, Request, status
from fastapi.responses import Response, PlainTextResponse

statuscheck_router = APIRouter()


@statuscheck_router.get("/")
def root() -> Dict[str, str]:
    return {'app': 'Dispenser', 'time': str(datetime.now())}


@statuscheck_router.get("/status-check")
def statuscheck(request: Request) -> Response:
    return PlainTextResponse(None, status.HTTP_200_OK, {'Location': request.url.path})
