import json
from datetime import timedelta
from pathlib import Path
from typing import Any

from fastapi.responses import Response

_STATIC_DIR = Path(__file__).parent / "static"


def load_json_file(filename: str) -> Any:
    path = _STATIC_DIR / filename

    with path.open(encoding="utf-8") as f:
        return json.load(f)


def static_json_endpoint(filename: str, cache_ttl: timedelta = timedelta(hours=12)):
    def endpoint(response: Response):
        response.headers["Cache-Control"] = (
            f"public, max-age={int(cache_ttl.total_seconds())}"
        )
        return load_json_file(filename)

    return endpoint
