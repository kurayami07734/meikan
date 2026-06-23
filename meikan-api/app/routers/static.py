from datetime import timedelta

from fastapi import HTTPException
from fastapi.responses import Response
from fastapi.routing import APIRouter

from app.schema.static import Profile, Project
from app.utils import load_json_file, static_json_endpoint

router = APIRouter(tags=["Static"])

router.add_api_route(
    "/profile",
    static_json_endpoint("profile.json"),
    methods=["GET"],
    summary="Get profile information",
    description="Returns the portfolio owner's profile data.",
    response_model=Profile,
)

router.add_api_route(
    "/projects",
    static_json_endpoint("projects.json"),
    methods=["GET"],
    summary="List project information",
    description="Returns the owner's projects.",
    response_model=list[Project],
)


@router.get("/projects/{slug}", response_model=Project)
async def get_project(response: Response, slug: str) -> Project:
    """
    Get project information for a specific project
    """
    projects = load_json_file("projects.json")

    response.headers["Cache-Control"] = (
        f"public, max-age={int(timedelta(hours=12).total_seconds())}"
    )

    for project in projects:
        if project["slug"] == slug:
            return project

    raise HTTPException(status_code=404, detail="Project not found")
