from fastapi.routing import APIRouter

from app.schema.static import Profile
from app.utils import static_json_endpoint

router = APIRouter(tags=["Static"])

router.add_api_route(
    "/profile",
    static_json_endpoint("profile.json"),
    methods=["GET"],
    summary="Get profile information",
    description="Returns the portfolio owner's profile data.",
    response_model=Profile,
)
