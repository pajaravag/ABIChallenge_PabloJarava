from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.models.features import PayloadFeatures, SurvivedResponse
from src.pipeline.inference import predict

router = APIRouter()


@router.post("/predict", status_code=200, response_model=SurvivedResponse)
def predict_route(payload: PayloadFeatures) -> JSONResponse:
    """Make a prediction given the request payload.

    Parameters:
        payload (PayloadFeatures): request payload

    Returns:
        JSONResponse: prediction
    """

    payload = payload.dict()
    prediction = predict(payload)
    response = SurvivedResponse(survived=prediction)

    return JSONResponse(content=response.model_dump())
