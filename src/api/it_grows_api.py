import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.services.it_grows_service import ItGrowsService
from src.models.coordenates_dto import CoordenatesDTO

router = APIRouter()

@router.post("/it-grows")
async def what_grows(dto: CoordenatesDTO):
    it_grows_service = ItGrowsService()
    response = it_grows_service.what_grows(dto)
    data = json.loads(response)
    
    return JSONResponse(content=data)