from pydantic import BaseModel

class ForecastResponse(BaseModel):
    temperature: float
    wind_speed: float
    cloud_cover: int


