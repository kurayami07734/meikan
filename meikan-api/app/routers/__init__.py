from fastapi.routing import APIRouter

from app.routers.static import router as static_router

base_router = APIRouter()

base_router.include_router(static_router)


@base_router.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok"}
