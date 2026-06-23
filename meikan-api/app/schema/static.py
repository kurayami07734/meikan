from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field, HttpUrl


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


class ProjectType(StrEnum):
    PERSONAL = "personal"
    PROFESSIONAL_CASE_STUDY = "professional_case_study"
    OPEN_SOURCE = "open_source"
    ARCHIVED = "archived"
    LAB = "lab"


class ProjectStatus(StrEnum):
    ACTIVE = "active"
    COMPLETED = "completed"
    SHIPPED = "shipped"
    PROTOTYPE = "prototype"
    NEAR_PRODUCTION_PROTOTYPE = "near-production prototype"
    ARCHIVED = "archived"


class ProjectVisibility(StrEnum):
    PUBLIC = "public"
    CASE_STUDY = "case-study"
    PRIVATE = "private"


class ProjectLink(BaseModel):
    label: str = Field(..., examples=["GitHub"])
    url: HttpUrl


class Project(BaseModel):
    slug: Annotated[
        str,
        Field(
            pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
            examples=["utabridge"],
        ),
    ]
    title: str = Field(..., examples=["Utabridge"])
    subtitle: str
    type: ProjectType
    status: ProjectStatus
    featured: bool = False
    visibility: ProjectVisibility = ProjectVisibility.PUBLIC

    summary: str
    problem: str
    solution: str
    impact: list[str] = Field(default_factory=list)

    tech_stack: list[str] = Field(default_factory=list)
    links: list[ProjectLink] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)


ProjectsResponse = list[Project]


class Hobby(BaseModel):
    slug: str
    name: str
    summary: str
    highlights: list[str]


class Social(BaseModel):
    label: str
    url: HttpUrl
    username: str
    category: str
