import multiprocessing

from src.apps.dispenser.backend.server import run_dispenser_backend

dispenser_backend_process = multiprocessing.Process(target=run_dispenser_backend)
