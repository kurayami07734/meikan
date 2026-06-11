from httpx import AsyncClient

from app.schema.static import Profile


async def test_get_profile(client: AsyncClient):
    response = await client.get("/api/profile")

    assert response.status_code == 200
    assert response.headers["Cache-Control"] == "public, max-age=43200"

    Profile.model_validate(response.json())
