from pydantic import BaseModel, HttpUrl


class Link(BaseModel):
    label: str
    url: HttpUrl


class Profile(BaseModel):
    name: str
    headline: str
    subheadline: str
    location: str
    bio: str
    links: list[Link]
