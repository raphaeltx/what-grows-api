from pydantic import BaseModel

class CoordenatesDTO(BaseModel):
    latitude: str
    longitude: str