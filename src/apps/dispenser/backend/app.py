from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apps.dispenser.backend.routers.statuscheck_router import statuscheck_router

dispenser_backend_app = FastAPI()

dispenser_backend_app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

dispenser_backend_app.include_router(statuscheck_router)
