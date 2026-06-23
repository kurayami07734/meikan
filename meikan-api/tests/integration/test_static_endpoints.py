from httpx import AsyncClient

from app.schema.static import Profile, Project


async def test_get_profile(client: AsyncClient):
    response = await client.get("/api/profile")

    assert response.status_code == 200
    assert response.headers["Cache-Control"] == "public, max-age=43200"

    Profile.model_validate(response.json())


async def test_get_project_by_unknown_slug_returns_404(client: AsyncClient):
    response = await client.get("/api/projects/does-not-exist")

    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}


async def test_get_projects(client: AsyncClient):
    response = await client.get("/api/projects")

    assert response.status_code == 200
    assert response.headers["Cache-Control"] == "public, max-age=43200"

    projects = response.json()

    assert isinstance(projects, list)
    assert len(projects) > 0

    for project in projects:
        Project.model_validate(project)


async def test_get_project_by_slug(client: AsyncClient):
    projects_response = await client.get("/api/projects")
    projects = projects_response.json()
    slug = projects[0]["slug"]

    response = await client.get(f"/api/projects/{slug}")

    assert response.status_code == 200
    assert response.headers["Cache-Control"] == "public, max-age=43200"

    project = Project.model_validate(response.json())

    assert project.slug == slug
