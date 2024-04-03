from fastapi import FastAPI
from app.api.main import api_router
from . import data
app = FastAPI(
    title="Project_name"
)

app.include_router(api_router)