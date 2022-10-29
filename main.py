from app.routers import tasks_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(tasks_router.router)