from app.config import apps
from app.models.tracking import InputTracking, OutPutTracking
from app.usecases.tracking import track_logic

@apps.app.get("/")
async def wellcome() -> list:
    return {
        "details":"this micro web service in used for tracking post packets"
    }
    


@apps.app.post('/track', response_model=OutPutTracking)
async def track(input:InputTracking) -> OutPutTracking:
    return track_logic(input)
   