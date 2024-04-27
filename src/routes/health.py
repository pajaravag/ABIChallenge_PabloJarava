from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/health", status_code=200)
async def health() -> JSONResponse:
    """Health check endpoint
    Returns:
        JSONResponse: status ok
    """
    return {"status": "ok"}
