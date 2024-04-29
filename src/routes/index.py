import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/", status_code=200)
def read_root() -> JSONResponse:
    """Root endpoint
    Returns:
        JSONResponse: Hello World
    """
    return JSONResponse(content=json.dumps({"Hello": "World"}))
