from fastapi import FastAPI

from app.routers import base_router

app = FastAPI()

app.include_router(prefix="/api", router=base_router)



