from fastapi import FastAPI

from app.routers import base_router

app = FastAPI(
    title="Meikan API",
    description="API for the Meikan portfolio platform.",
    version="0.0.1",
    contact={
        "name": "Aditya Ghidora",
        "url": "https://ghidora.dev",
    },
)

app.include_router(prefix="/api", router=base_router)
