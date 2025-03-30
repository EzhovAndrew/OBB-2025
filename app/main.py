"""Main service module."""

from fastapi import FastAPI
from rest.api import router

app = FastAPI()

app.include_router(router)
